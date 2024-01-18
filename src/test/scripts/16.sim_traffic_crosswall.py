#!/usr/bin/env phython3
#-*- coding:utf-8 -*-



import rospy
from morai_msgs.msg import GetTrafficLightStatus
from std_msgs.msg import Float64
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage,LaserScan
import cv2
import numpy as np
from time import *
from math import *

class Traffic_control:
    def __init__(self):
        rospy.init_node("Line_sub_node")
        self.speed_pub = rospy.Publisher("/commands/motor/speed",Float64,queue_size=1)
        self.steer_pub = rospy.Publisher("/commands/servo/position",Float64,queue_size=1)
        rospy.Subscriber("/GetTrafficLightStatus",GetTrafficLightStatus,self.traffic_CB)
        rospy.Subscriber("/image_jpeg/compressed",CompressedImage,self.cam_CB)
        rospy.Publisher("/Lidar2D",LaserScan,self.lidar_CB,queue_size=1)
        self.bridge = CvBridge()
        self.speed_msg = Float64()
        self.steer_msg = Float64()
        self.traffic_msg = GetTrafficLightStatus()
        self.traffic_flag = 0
        self.prev_signal = 0
        self.signal = 0
        self.cross_flag = 0
        self.img = []
        self.center_index = 0
        self.standard_line = 0 
        self.degree_per_pixel = 0
        self.steer = 0.5
        self.obstacle_flag = False

    def traffic_CB(self,msg):
        self.traffic_msg = msg
        if self.traffic_msg.trafficLightIndex == "SN000002":
            signal = self.traffic_msg.trafficLightStatus
            if self.prev_signal != signal:
                self.prev_signal = signal
            # first_time = time()
            self.traffic_think()
            # second_time = time()
            # print(f"different:{second_time-first_time}")

    def traffic_think(self):
        if self.signal == 1:
            print("red")
        elif self.signal == 4:
            print("yellow")
        elif self.signal == 16:
            print("green")
        elif self.signal == 33:
            print("left")
        else:
            pass

    def cam_CB(self,msg):
        self.img = self.bridge.compressed_imgmsg_to_cv2(msg)
        self.warped_img, self.center_index, self.standard_line, self.degree_per_pixel = self.cam_lane_detection()

    def cam_lane_detection(self): 
        y,x = self.img.shape[0:2]
        img_hsv = cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(img_hsv)
        yellow_lower = np.array([15,128,0])
        yellow_upper = np.array([45,255,255])
        yellow_range = cv2.inRange(img_hsv,yellow_lower,yellow_upper)
        white_lower = np.array([0,0,192])
        white_upper = np.array([179,64,255])
        white_range = cv2.inRange(img_hsv,white_lower,white_upper)
        combined_range = cv2.bitwise_or(yellow_range,white_range)
        filtered_img = cv2.bitwise_and(self.img,self.img,mask = combined_range)

        src_point1 = [0,420]
        src_point2 = [275,260]
        src_point3 = [x - 275,260]
        src_point4 = [x,420]
        src_points = np.float32([src_point1,src_point2,src_point3,src_point4])
       
        dst_point1 = [x//4,480]
        dst_point2 = [x//4,0]
        dst_point3 = [x//8*7,0]
        dst_point4 = [x//8*7,480]
        dst_points = np.float32([dst_point1,dst_point2,dst_point3,dst_point4])

        matrix = cv2.getPerspectiveTransform(src_points,dst_points)
        warped_img = cv2.warpPerspective(filtered_img,matrix,(x,y))
        grayed_img = cv2.cvtColor(warped_img,cv2.COLOR_BGR2HSV)
        bin_img = np.zeros_like(grayed_img)
        bin_img[grayed_img>50] = 1
        histogram_x = np.sum(bin_img,axis=0)
        histogram_y = np.sum(bin_img,axis=1)
        
        left_hist = histogram_x[0:x//2]
        right_hist = histogram_x[x//2:]
        up_hist = histogram_y[0:y//4*3]
        down_hist = histogram_y[y//4*3:]
        left_indeices = np.where(left_hist>20)[0]
        right_indeices = np.where(right_hist>20)[0] + 320
        cross_indices = np.where(down_hist>400)[0] + 240
        try: 
            cross_threshold = 25
            cross_diff = cross_indices[-1] - cross_indices[0]
            if cross_threshold < cross_diff:
                self.cross_flag = True
                cv2.rectangle(warped_img,[0,cross_indices[0]],[x,cross_indices[-1]],[0,255,0],3) 
        
            else:
                self.cross_flag = False
        except:
            self.cross_flag = False

        indices = np.where(histogram_x>20)[0]
        print("left_indices",left_indeices)
        print("right_indices",right_indeices)
        print("check",len(left_indeices))

        try:
            if len(left_indeices)!=0 and len(right_indeices)!=0:
                center_index = (indices[0]+indices[-1])//2
                print("both_line")
            elif len(left_indeices) !=0 and len(right_indeices)==0:
                center_index = (left_indeices[0]+left_indeices[-1])//2
                print("left_line")
            elif len(left_indeices) ==0 and len(right_indeices)!=0:
                center_index = (right_indeices[0]+right_indeices[-1])//2
                print("right_line")
                
        except:
            center_index = x//2
        
        standard_line = x//2
        degree_per_pixel = 1/x
        return warped_img, center_index, standard_line, degree_per_pixel
    
    def lidar_CB(self,msg):
        # os.system("clear")
        self.scan_msg = msg
        self.steer = self.obstacle()

    def obstacle(self):
        degree_min = self.scan_msg.angle_min = 180/pi
        degree_max = self.scan_msg.angle_max *180/pi
        degree_angle_increment = self.scan_msg.angle_increment *180/pi
        print(self.scan_msg)
        print(degree_angle_increment)
        print(len(self.scan_msg.ranges))
        # self.scan_msg.ranges 
        degrees = []
        degrees = [degree_min + degree_angle_increment *index for index, value in enumerate(self.scan_msg.ranges)] 
        # degree_array = np.array(degrees)
        # print(np.where((degree_array)<90.1)[0])
        obstacle_degrees = []
        obstacle_index = []
        for index, value in enumerate(self.scan_msg.ranges):
            if abs(degrees[index])<90 and 0<value<1.5:
                obstacle_degrees.append(degrees[index])
                obstacle_index.append(index)
            else :
                pass
       
        try:
            right_space = obstacle_index[0] - 180
            left_space = 542 - obstacle_index[-1]
            if right_space > left_space:
                print(f"right:{obstacle_index[0]}")
                right_index_avg = (degrees(obstacle_index[0])-90)/2
                print(f"right_degree_avg:{right_index_avg}")
                degree_avg = right_index_avg
            else:
                print(f"left:{obstacle_index[-1]}")
                left_index_avg = (degrees(obstacle_index[-1])+90)/2
                print(f"left_degree_avg:{left_index_avg}")
                degree_avg = left_index_avg
            self.obstacle_flag = True
            steer = ((-degree_avg/90) + 0.5)/2
        except:
            self.obstacle_flag = False
            degree_avg = 0
            steer = 0.5
        return steer

    
    def action(self):
        if len(self.img) != 0:
            if self.cross_flag == True and self.signal == 1:
                speed = 0
                steer = 0.5
            else:
                if self.obstacle_flag == True:
                    steer = self.steer
                    speed = 500
                else:
                    steer = (self.center_index-self.standard_line) * self.degree_per_pixel
                    steer = (0.5 + steer*2)
                    speed = 1000
            # print(f"steer:{steer}")
            self.steer_msg.data  = steer
            self.speed_msg.data = speed
            self.steer_pub.publish(self.steer_msg)
            self.speed_pub.publish(self.speed_msg)
            cv2.imshow("img",self.img)
            cv2.imshow("warped_img",self.warped_img)
            cv2.waitKey(1)

def main():
    try:
        traffic_control = Traffic_control()
        while not rospy.is_shutdown():
            traffic_control.action()
    except rospy.ROSInterruptException:
        pass


if __name__=="__main__":
    main()
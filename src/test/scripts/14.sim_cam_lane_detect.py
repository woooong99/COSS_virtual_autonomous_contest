#!/usr/bin/env phyton3
#-*- coding:utf-8 -*-

import rospy
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Float64
from cv_bridge import CvBridge
import cv2
import numpy as np

class Line_sub:
    def __init__(self):
        rospy.init_node("Line_sub_node")
        rospy.Subscriber("/image_jpeg/compressed",CompressedImage,self.cam_CB)
        self.speed_pub = rospy.Publisher("/commands/motor/speed",Float64,queue_size=1)
        self.steer_pub = rospy.Publisher("/commands/servo/position",Float64,queue_size=1)
        self.image_msg = CompressedImage()
        self.bridge = CvBridge()
        self.speed_msg = Float64()
        self.steer_msg = Float64()
        self.cross_flag = 0

    def cam_CB(self,msg):
        img = self.bridge.compressed_imgmsg_to_cv2(msg)
        y,x = img.shape[0:2]
        img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(img_hsv)
        yellow_lower = np.array([15,128,0])
        yellow_upper = np.array([45,255,255])
        yellow_range = cv2.inRange(img_hsv,yellow_lower,yellow_upper)
        white_lower = np.array([0,0,192])
        white_upper = np.array([179,64,255])
        white_range = cv2.inRange(img_hsv,white_lower,white_upper)
        combined_range = cv2.bitwise_or(yellow_range,white_range)
        filtered_img = cv2.bitwise_and(img,img,mask = combined_range)

        # src_point1 = [0,420]
        # src_point2 = [275,260]
        # src_point3 = [x - 275,260]
        # src_point4 = [x,420]
        # src_points = np.float32([src_point1,src_point2,src_point3,src_point4])
       
        # dst_point1 = [x//4,480]
        # dst_point2 = [x//4,0]
        # dst_point3 = [x//8*7,0]
        # dst_point4 = [x//8*7,480]
        # dst_points = np.float32([dst_point1,dst_point2,dst_point3,dst_point4])


        matrix = cv2.getPerspectiveTransform(src_points,dst_points)
        #matrix = cv2.UMat(matrix)
        warped_img = cv2.warpPerspective(filtered_img,matrix,(x,y))
        grayed_img = cv2.cvtColor(warped_img,cv2.COLOR_BGR2HSV)
        bin_img = np.zeros_like(grayed_img)
        bin_img[grayed_img>50] = 1
        histogram = np.sum(bin_img,axis=0)
        left_hist = histogram[0:x//2]
        right_hist = histogram[x//2:]
        left_indeices = np.where(left_hist>20)[0]
        right_indeices = np.where(right_hist>20)[0] + 320
        indices = np.where(histogram>20)[0]
        # print("left_indices",left_indeices)
        # print("right_indices",right_indeices)
        # print("check",len(left_indeices))

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
            print("no_line")
        # canny_img = cv2.Canny(bin_img,2,2)
        # cv2.imshow("canny_img", canny_img)
        bin_img = cv2.cvtColor(bin_img, cv2.COLOR_BGR2GRAY)
        lines = cv2.HoughLinesP(bin_img,0.01,np.pi/180,90,50,5)
        
       
 
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(warped_img,(x1,y1), (x2,y2),(0,255,0),1)
            print(line)
            self.cross_flag == self.cross_flag+1
            print(self.cross_flag)
       
       
        # if lines is not None:
        #     for line in lines:
        #         x1,y1,x2,y2 = line[0]
        #         cv2.line(warped_img,(x1,y1), (x2,y2),(0,255,0),1)
        #         print(line)
        #         self.cross_flag == self.cross_flag+1
        #         print(self.cross_flag)
        # else:
        #     print("")




        # try:
            # center_index = (indices[0]+indices[-1])//2
        # except:
            # center_index = x//2
        # print(center_index)
    #    print(histogram[histogram!=0])
       
        standard_line = x//2
        degree_per_pixel = 1/x
        steer = (center_index-standard_line) * degree_per_pixel
        steer = 0.5 + steer
        print(f"steer:{steer}")
        self.steer_msg.data  = steer
        self.speed_msg.data = 1000
        self.steer_pub.publish(self.steer_msg)
        self.speed_pub.publish(self.speed_msg)

    #    print(histogram[0])
    #    cv2.imshow("bin_img",bin_img)

        cv2.imshow("img",img)
    #    cv2.imshow("yellow_range",yellow_range)
    #    cv2.imshow("white_range",white_range)
    #    cv2.imshow("combined_range",combined_range)
    #    cv2.imshow("filtered_img",filtered_img)
        cv2.imshow("warped_img",warped_img)
    #    cv2.imshow("img_hsv",img_hsv)
        cv2.waitKey(1)

def main():
    try:
        lane_sub = Line_sub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":
    main()
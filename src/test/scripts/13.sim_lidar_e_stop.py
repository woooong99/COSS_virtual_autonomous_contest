#!/usr/bin/env phyton3
#-*- coding:utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64
from math import *
import os

class Turtle_sub:
    def __init__(self):
        rospy.init_node("sim_e_stop")
        self.pub = rospy.Publisher("/commands/motor/speed",Float64,queue_size=1)
        self.pub = rospy.Publisher("/Lidar2D",LaserScan,self.lidar_CB)
        self.scan_msg = LaserScan()
        self.speed_msg = Float64()

    def lidar_CB(self,msg):
        os.system("clear")
        self.scan_msg = msg
        degree_min = self.scan_msg.angle_min = 180/pi
        degree_max = self.scan_msg.angle_max *180/pi
        degree_angle_increment = self.scan_msg.angle_increment *180/pi
        print(self.scan_msg)
        print(degree_angle_increment)
        print(len(self.scan_msg.ranges))
        # self.scan_msg.ranges 
        degrees = []
        degrees = [degree_min + degree_angle_increment *index for index, value in enumerate(self.scan_msg.ranges)] 
        obstacle_degrees = []
            # degree = degree_min + degree_angle_increment *index
            # degrees.append(degree)
        # print(degrees)
        for index, value in enumerate(self.scan_msg.ranges):
            if -30<degrees[index]<30 and 0<value<1.5:
                print(f"obstacle:{degrees[index]}")
                obstacle_degrees.append(degrees[index])
            else :
                pass

        print(len[obstacle_degrees])
        if len(obstacle_degrees) != 0:
            self.speed_msg.data = 0
        else: 
            self.speed_msg.data = 1200

        self.pub.publish(self.speed_msg)

def main():
    try:
        trutle_sub = Turtle_sub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":
    main()
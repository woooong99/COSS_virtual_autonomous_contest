#!/usr/bin/env phyton3
#-*- coding:utf-8 -*-

import rospy
from turtlesim.msg import Pose,Color

class Turtle_sub:
    def __init__(self):
        rospy.init_node("turtle_sub_node")
        rospy.Subscriber("/turtle1/pose",Pose,self.turtle_pose_CB)
        rospy.Subscriber("/turtle1/Color",Color,self.turtle_color_CB)
        self.pose_msg = Pose()

    def turtle_pose_CB(self,msg):
        print("---pose---")
        self.pose_msg = msg
        print(self.pose_msg)

    def turtle_color_CB(self,msg):
        print("---color---")
        self.color_msg = msg
        print(self.color_msg)
       

def main():
    try:
        trutle_sub = Turtle_sub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":
    main()

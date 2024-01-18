#!/usr/bin/env phyton3
#-*- coding:utf-8 -*-

import rospy
from turtlesim.msg import Pose,Color
from geometry_msgs.msg import Twist

class Turtle_sub:
    def __init__(self):
        rospy.init_node("turtle_sub_node")
        rospy.Subscriber("/turtle1/pose",Pose,self.turtle_pose_CB)
        rospy.Subscriber("/turtle1/Color",Color,self.turtle_color_CB)
        self.pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=1)
        self.pose_msg = Pose()
        self.cmd_msg = Twist() 
        self.color_msg = Color()
        self.rate = rospy.Rate(1)
        
    def func(self):
        if 1 < self.pose_msg.x < 10 and 1 < self.pose_msg.y < 10:
            self.cmd_msg.linear.x = 1
            self.cmd_msg.angular.z = 0
        else:
            self.cmd_msg.linear.x = 0.5
            self.cmd_msg.angular.z = 0.5

        self.pub.publish(self.cmd_msg)
        self.rate.sleep()
         
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
        turtle_pub = Turtle_sub()
        while not rospy. is_shutdown():
            turtle_pub.func()
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":
    main()
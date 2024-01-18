#!/usr/bin/env phyton3
#-*- coding:utf-8 -*-

import rospy
from std_msgs.msg import Float64

class Turtle_sub:
    def __init__(self):
        rospy.init_node("sim_cmd_node")
        self.pub = rospy.Publisher("/commands/servo/position",Float64,queue_size=1)
        self.cmd_msg = Float64()
        self.rate = rospy.Rate(2)
        self.steer = 0 #vaule : 0~1 -> degree : -19.5 ~ 19.5 

    def func(self):
        self.steer += 0.01
        if self.steer >=1:
            self.steer = 1
        self.cmd_msg.data = ((self.steer/19.5)+1)/2
        self.pub.publish(self.cmd_msg)
        self.rate.sleep()
        print(f"steer:{self.cmd_msg.data})")
def main():
    try:
        turtle_pub = Turtle_sub()
        while not rospy. is_shutdown():
            turtle_pub.func()
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":
    main()
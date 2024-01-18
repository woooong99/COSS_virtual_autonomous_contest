#!/usr/bin/env phyton3
#-*- coding:utf-8 -*-

import rospy
from std_msgs.msg import Float64

class Turtle_sub:
    def __init__(self):
        rospy.init_node("sim_cmd_node")
        self.pub = rospy.Publisher("/commands/motor/speed",Float64,queue_size=1)
        self.cmd_msg = Float64()
        self.rate = rospy.Rate(2)
        self.speed = 0

    def func(self):
        self.speed += 1
        self.speed % 2401
        self.cmd_msg.data = self.speed
        self.pub.publish(self.cmd_msg)
        self.rate.sleep()
        print(f"speed:{self.cmd_msg.data})")
def main():
    try:
        turtle_pub = Turtle_sub()
        while not rospy. is_shutdown():
            turtle_pub.func()
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":
    main()
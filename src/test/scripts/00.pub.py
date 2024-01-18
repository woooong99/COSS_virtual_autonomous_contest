#!/usr/bin/env phyton3
#-*- coding:utf-8 -*-

import rospy
from std_msgs.msg import Int32

rospy.init_node("wego_pub_node") 
pub = rospy.Publisher("/counter",Int32,queue_size=1)
int_msg = Int32()
rate = rospy.Rate(1)
num = 0
while not rospy.is_shutdown():
    num=num+1
    int_msg.data = num
    pub.publish(int_msg)
    print(num)
    rate.sleep()
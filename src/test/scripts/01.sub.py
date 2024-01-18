#!/usr/bin/env phyton3
#-*- coding:utf-8 -*-

import rospy
from std_msgs.msg import Int32

def CB(msg):
    num = msg.data*2
    print(num)

rospy.init_node("wego_sub_node")
rospy.Subscriber("counter",Int32,CB)
rospy.spin()
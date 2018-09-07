#!/usr/bin/env python

from __future__ import print_function

import rospy
from sensor_msgs.msg import LaserScan

class ReceiveMessageNode(object):
    def __init__(self):
        rospy.init_node('receive_message_node')
        rospy.Subscriber('/scan', LaserScan, self.process_scan)

    def process_scan(self, m):
        print(m.ranges[0])

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = ReceiveMessageNode()
    node.run()

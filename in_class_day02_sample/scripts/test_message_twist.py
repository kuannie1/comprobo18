#!/usr/bin/env python

from __future__ import print_function
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Header
import rospy

class TestMessageNode(object):
    """ This node publishes a message at 2 Hz """
    def __init__(self):
        rospy.init_node("test_node")
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def run(self):
        r = rospy.Rate(2)
        while not rospy.is_shutdown():
            m = Twist(linear=Vector3(x=0, y=0, z=0), angular=Vector3(x=0, y= 0, z=0.5))
            self.pub.publish(m)
            r.sleep()


if __name__ == '__main__':
    node = TestMessageNode()
    node.run()

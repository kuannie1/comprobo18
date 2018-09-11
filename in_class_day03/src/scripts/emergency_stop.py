#!/usr/bin/env python
from __future__ import print_function, division
from std_msgs.msg import Header
import rospy
from neato_node.msg import Bump # this import is needed for Bump sensors
from geometry_msgs.msg import Twist, Vector3
from geometry_msgs.msg import PointStamped 
# find the right packages from running something like 
# 'rostopic list' 
# 'rostopic info /cmd_vel' for subscriber
# 'rosmsg show geometry_msgs/Twist' for publisher

class EmergencyStopNode(object):
	""" This node moves forward at a fixed pace and stops when the bump sensor is triggered """
	def __init__(self):
		self.bump = False
		rospy.init_node('receive_message_node')
		rospy.Subscriber('/bump', Bump, self.process_scan)
		self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

	def process_scan(self, m):
		bump1 = m.leftSide
		bump2 = m.rightSide
		bump3 = m.leftFront
		bump4 = m.rightFront
		self.bump = bump1 or bump2 or bump3 or bump4

	def run(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			if (self.bump):
				self.pub.publish(Twist())
			else:
				m = Twist(linear=Vector3(x=.2, y=0, z=0), angular=Vector3(x=0, y= 0, z=0))
				self.pub.publish(m)
			r.sleep()

if __name__ == '__main__':
    node = EmergencyStopNode()
    node.run()
		

#!/usr/bin/env python
from __future__ import print_function, division
from std_msgs.msg import Header
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Vector3
from geometry_msgs.msg import PointStamped # find the right packages from running something like 'rostopic info /cmd_vel' or 'rosmsg show geometry_msgs/Twist'

class EmergencyStopNode(object):
    """ This node moves forward at a fixed pace and stops when it detects an object within a certain distance. """
    def __init__(self, threshold):
	self.objdistance = 10
        rospy.init_node('receive_message_node')
        rospy.Subscriber('/scan', LaserScan, self.process_scan)
	self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	self.threshold = threshold

    def process_scan(self, m):
        self.objdistance = m.ranges[0]
	print(self.objdistance)
	print("threshold: ", self.threshold)

    def run(self):
	r = rospy.Rate(10)
	while not rospy.is_shutdown():
		if self.objdistance > self.threshold:
			m = Twist(linear=Vector3(x=.2, y=0, z=0), angular=Vector3(x=0, y= 0, z=0))
			self.pub.publish(m)

		else:
			self.pub.publish(Twist())
			#rospy.spin()
		r.sleep()


if __name__ == '__main__':
    node = EmergencyStopNode(.5)
    node.run()

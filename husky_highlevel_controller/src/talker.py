#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker')
	rate = rospy.Rate(1)

	counter = 0

	while not rospy.is_shutdown():
		msg = "Hello Rospy: {}".format(counter)
		rospy.loginfo(msg)
		pub.publish(msg)
		rate.sleep()
		counter+=1

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		print("Some error occured!")
		pass

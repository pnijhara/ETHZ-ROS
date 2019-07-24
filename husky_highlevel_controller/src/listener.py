#!/usr/bin/env python

import rospy
import os
# from std_msgs.msg import String
from sensor_msgs.msg import LaserScan


def callback(msg):
    os.system('clear')
    rospy.loginfo(" Distance: {}\n"
                  .format(msg.ranges[len(msg.ranges) / 2]))


def listener():
    rospy.init_node('listener')
    topicName = rospy.get_param('~topic')
    queueSize = rospy.get_param('~queue')
    rospy.Subscriber(name=topicName, data_class=LaserScan,
                     callback=callback, queue_size=queueSize)
    rospy.spin()


if __name__ == '__main__':
    listener()

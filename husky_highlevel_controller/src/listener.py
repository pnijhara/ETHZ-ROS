#!/usr/bin/env python

import rospy
import os
from sensor_msgs.msg import LaserScan


def callback(msg):
    print len(msg.ranges)

def listener():
    rospy.init_node('listener')
    topicname = rospy.get_param('~topic')
    queueSize = rospy.get_param('~queue')
    rospy.Subscriber(
                    name=topicname,
                    data_class=LaserScan,
                    callback=callback,
                    queue_size=queueSize
                    )
    rospy.spin()


if __name__ == '__main__':
    listener()

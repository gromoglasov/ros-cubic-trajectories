#!/usr/bin/env python

import rospy
import random

from AR_week5_test.msg import cubic_traj_params

def points_generator():
    # initialise new topic
    pub = rospy.Publisher('points', cubic_traj_params, queue_size=0)
    # initialise new node
    rospy.init_node('points_generator', anonymous=True)
    rate = rospy.Rate(0.05) # 0.05hz or once every 20 seconds
    msg = cubic_traj_params()
    while not rospy.is_shutdown():
        # generate random numbers
        msg.p0 = random.uniform(-10, 10)
        msg.pf = random.uniform(-10, 10)
        msg.v0 = random.uniform(-10, 10)
        msg.vf = random.uniform(-10, 10)
        msg.t0 = 0
        msg.tf = msg.t0 + round(random.uniform(5, 10), 0)
        rospy.loginfo(msg)
        pub.publish(msg)
        print(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        points_generator()
    except rospy.ROSInterruptException:
        pass

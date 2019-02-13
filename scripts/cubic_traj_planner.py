#!/usr/bin/env python
import rospy
from AR_week5_test.srv import *
from AR_week5_test.msg import cubic_traj_params
from AR_week5_test.msg import cubic_traj_coeffs


def callback(data):
    # publishing initialised
    pub = rospy.Publisher('coeffs', cubic_traj_coeffs, queue_size=0)

    try:
        # try to connect to service 
        compute = rospy.ServiceProxy('compute_service', compute_cubic_traj)
        # compute tajectories using data obtained from the subscriber
        resp = compute(data)

        # construct a message
        msg = cubic_traj_coeffs()
        msg.a0 = resp.a0
        msg.a1 = resp.a1
        msg.a2 = resp.a2
        msg.a3 = resp.a3
        msg.t0 = data.t0
        msg.tf = data.tf
    # publish obtained data
        print msg
        pub.publish(msg)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def cubic_traj_planner():
    # initialise new node
    rospy.init_node('cubic_traj_planner', anonymous=True)
    # wait for service
    rospy.wait_for_service('compute_service')
    # subscribe to cubic_traj_params and send data to callback
    rospy.Subscriber('points', cubic_traj_params, callback)
    # prevent from dying
    rospy.spin()


if __name__ == "__main__":
    cubic_traj_planner()
    


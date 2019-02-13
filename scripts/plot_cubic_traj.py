#!/usr/bin/env python
import rospy

from AR_week5_test.msg import cubic_traj_coeffs
from AR_week5_test.msg import position_trajectory
from AR_week5_test.msg import velocity_trajectory
from AR_week5_test.msg import acceleration_trajectory


def callback(data):
    # publishing initialised
    pub1 = rospy.Publisher('position_trajectory', position_trajectory, queue_size=0)
    pub2 = rospy.Publisher('velocity_trajectory', velocity_trajectory, queue_size=0)
    pub3 = rospy.Publisher('acceleration_trajectory', acceleration_trajectory, queue_size=0)
    
    # initialise messages
    msg1 = position_trajectory()    
    msg2 = velocity_trajectory()
    msg3 = acceleration_trajectory()

    # calculate trajectories
    msg1.trj = data.a0 + data.a1 * data.tf + data.a2 * (data.tf**2) + data.a3 * (data.tf**3)
    msg2.trj = data.a1 + 2 * data.a2 * data.tf + 3 * data.a3 * (data.tf**2)
    msg3.trj = 2 * data.a2 + 6 * data.a3 * data.tf
    # publish messages
    print('Publishing trajectories %d, %d, %d' % (msg1.trj, msg2.trj, msg3.trj))
    pub1.publish(msg1)
    pub2.publish(msg2)
    pub3.publish(msg3)

def plot_cubic_traj():
    # initialise new node
    rospy.init_node('plot_cubic_traj', anonymous=True)
    # subscribe to cubic_traj_params and send data to callback
    rospy.Subscriber('coeffs', cubic_traj_coeffs, callback)
    # prevent from dying
    rospy.spin()

if __name__ == "__main__":
    try:
        plot_cubic_traj()
    except rospy.ROSInterruptException:
        pass


#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

class BatteryLevelListener():
    def __init__(self, robot_no):
        rospy.init_node("battery_listener_" + str(robot_no))
        self.battery_sub = rospy.Subscriber('/battery_level_' + str(robot_no), Float32, self.store_battery_level_cb)
        self.array = list()

    def store_battery_level_cb(self, msg):
        """
        Callback for storing subscribed battery level message into an array
        :param msg:
        :return:
        """
        self.array.append(msg)

    def save_recorded_array(self, t_operation=30):
        """
        Return the stored array of length t_operation
        :param t_operation:
        :return:
        """
        while True:
            if len(self.array) >= t_operation:
                break
            else:
                pass
        return self.array
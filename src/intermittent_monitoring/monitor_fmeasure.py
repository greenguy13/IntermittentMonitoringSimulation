#!/usr/bin/env python

"""
Subscriber to the levels of F-measure
"""

import rospy
from std_msgs.msg import Float32



class FMeasureListener():
    def __init__(self, area):
        """
        Listens to F-measure
        :param duration: Length of operation/duration to store F-measure
        """
        rospy.init_node('fmeasure_listener_' + str(area))
        self.fmeasure_sub = rospy.Subscriber('/fmeasure_' + str(area), Float32, self.store_fmeasure)
        self.array = list()

    def store_fmeasure(self, msg):
        """
        Callback for storing subscribed F-measure message into an array
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
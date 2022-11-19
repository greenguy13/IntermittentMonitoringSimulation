#!/usr/bin/env python

import math

global max_fmeasure
global fsafe
max_fmeasure = 100
fsafe = 80

def decay(rate, t):
    """
    Decay function
    :param rate:
    :param t:
    :return:
    """
    decayed_fmeasure = max_fmeasure*(1.0 - rate)**t
    return decayed_fmeasure

def get_time_given_decay(decayed_fmeasure, rate):
    """
    Retrieves time given decayed measure and decay rate (by inversion)
    :param decayed_measure:
    :param rate:
    :return:
    """
    t = math.log((decayed_fmeasure/max_fmeasure), 1.0-rate)

    return t

def beta_rate(rate, rates):
    """
    Computes the normalized F-measure decay rate, which then is the Loss growth rate
    :param rate (float): decay rate
    :param rates (list): list of decay rates
    :return:
    """
    beta = rate / sum(rates)
    return beta

def compute_loss(decayed_fmeasure, rate, rates, est_duration):
    """
    Computes loss by estimating the decayed fmeasure given the decay rate after a set duration
    :param decayed_fmeasure:
    :param rate:
    :param duration:
    :return:
    """
    t0 = get_time_given_decay(decayed_fmeasure, rate)
    t = t0 + est_duration
    est_decayed_fmeasure = decay(rate, t)

    if est_decayed_fmeasure < fsafe:
        diff = fsafe - est_decayed_fmeasure
    else:
        diff = 0

    beta = beta_rate(rate, rates)

    loss = -beta*diff**2

    return loss


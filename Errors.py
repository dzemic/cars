#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CarError(Exception):
    """Basic exception for errors raised by cars"""
    def __init__(self, car, msg=None):
        if msg is None:
            # Set some default useful error message
            msg = 'An error occured with car %s' % car
        super(CarError, self).__init__(msg)
        self.car = car
        self.msg = msg

    def __str__(self):
        return self.msg

class CarCrashError(CarError):
    """When you drive too fast"""
    def __init__(self, car, other_car, speed):
        super(CarCrashError, self).__init__(
            car, msg = "Car crashed into %s at speed %d" % (other_car, speed))
            #msg = "Car crashed into %s at speed %d" % (other_car, speed))
        self.speed = speed
        self.other_car = other_car

    def __str__(self):
        return str(self.speed) + " " + self.other_car
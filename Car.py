#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, time
import Errors
import logging
logger = logging.getLogger(__name__)

class Car():
    """Car"""
    def __init__(self, car=None, max_speed=0, driver=None, car_pool=None):
        self.other_cars = car_pool
        self.car = car if car else random.choice(self.other_cars)
        self.driver = driver if driver else 'Mr Bean'
        self.max_speed = max_speed
        self.running = False

    def car_start(self):
        self.running = True

    def car_drive(self, max_speed):
        PATH_START = 0
        PATH_END = 1000

        start = time.time()
        PERIOD_OF_TIME = 10  # 10sec

        self.car_start()
        if max_speed:
            self.current_max_speed = max_speed
        current_speed = 0
        other_car = 'all clear'
        random_error_code = 0
        logger.info('Welcome to %s driving experiance. You are : %s driver(MAX %skm/h)\n' % (self.driver, self.car, self.max_speed))
        while True:
            random_error_code = random.randint(0, 100)
            logger.info('%s speeding up : %dkm/h, obsticle: %s' % (self.car, current_speed, other_car))
            time.sleep(1)
            current_speed = current_speed + 10

            if random_error_code > 90:
                self.car_stop()
                raise Errors.CarError(self.car)
            else:
                if current_speed > self.max_speed:
                    other_car = random.choice(self.other_cars)
                    logger.info('%s speeding up : %dkm/h, obsticle: %s' % (self.car, current_speed, other_car))
                    self.car_stop()
                    raise Errors.CarCrashError(self.car, other_car, current_speed)
                else:
                    logger.info('Driving %s. You are : %s\n' % (self.car, self.driver))
                    if time.time() > start + PERIOD_OF_TIME: break
        return self.car + ' success !!!'

    def car_stop(self):
        self.running = False

    def __str__(self):
        return self.car
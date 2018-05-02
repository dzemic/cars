#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import logging
import Errors
from Arena import Arena
from Car import Car
from Driver import Driver
from concurrent.futures import ProcessPoolExecutor
import json
from pprint import pprint

file_handler = logging.FileHandler(filename='tmp.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=handlers
)

logger = logging.getLogger('RACE')

def start(vehicle, driver, car_pool, cfg):
    try:
        d = Driver(driver, 35)
        c = Car(vehicle, 200, d, car_pool)
        #a.add_driver(d.name)
        result = c.car_drive(None)
    except Errors.CarCrashError as e:
        # If we crash at high speed, we call emergency
        if e.speed >= 30:
            d.call('911', e.msg)
        result = vehicle + ' failed (CarCrash)'
    except Errors.CarError as e:
        logger.error(e.msg)
        d.call('adac', e.msg)
        result = vehicle + ' failed (CarError)'
    return result

def main():

    cfg = json.load(open('./config/cars.json'))

    print(cfg["BMW"]["max_speed"])
    car_pool = [k for k, v in cfg.items()]
    driver_pool = [v["driver"] for k, v in cfg.items()]

    with ProcessPoolExecutor(max_workers=len(car_pool)) as executor:
        for driver, result in zip(driver_pool, executor.map(start, car_pool, driver_pool, car_pool, cfg)):
            print(result + ' with driver: ' + driver)

if __name__=='__main__':
    sys.exit(main())
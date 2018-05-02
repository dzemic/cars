#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Errors
import Driver
import logging
logger = logging.getLogger(__name__)

class Arena():
    """Arena"""
    def __init__(self, arena_name=None):
        self.length = 0
        if arena_name is 'easy' or None:
            self.length = 10
        elif arena_name is 'medium':
            self.length = 50
        elif arena_name is 'medium':
            self.length = 100

    def add_driver(self, driver):
        print('Driver %s is joining.' % driver)
        pass

    def __str__(self):
        return self.length
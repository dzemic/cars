#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, time
import Errors
import logging
logger = logging.getLogger(__name__)

class Race():
    """Driver"""
    def __init__(self, car=None):
        self.car = car if car else 'unknown'
        self.total = 2000

    def __str__(self):
        return self.car
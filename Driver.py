#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, time
import Errors
import logging
logger = logging.getLogger(__name__)

class Driver():
    """Driver"""
    def __init__(self, name=None, age=None):
        if age is None:
            age = 10
        self.age = age
        if name is None:
            name = 'Mr Bean'
        self.name = name

    def call(self, authority, reason):
        logger.info('[%s] - calling %s...' % (authority, authority))
        logger.info('[%s] - %s' % (authority, reason))

    def __str__(self):
        return self.name
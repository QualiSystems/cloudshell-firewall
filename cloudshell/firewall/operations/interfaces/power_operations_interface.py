#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
from abc import abstractmethod


class PowerOperationsInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def shutdown(self):
        pass

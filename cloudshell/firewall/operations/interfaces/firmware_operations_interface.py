#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
from abc import abstractmethod


class FirmwareOperationsInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def load_firmware(self, path):
        pass

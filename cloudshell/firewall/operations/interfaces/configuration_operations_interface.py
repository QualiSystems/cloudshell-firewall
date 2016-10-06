#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
from abc import abstractmethod


class ConfigurationOperationsInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def save(self, folder_path, configuration_type):
        pass

    @abstractmethod
    def restore(self, path, configuration_type, restore_method):
        pass

    @abstractmethod
    def orchestration_restore(self, saved_artifact_info, custom_params=None):
        pass

    @abstractmethod
    def orchestration_save(self, mode="shallow", custom_params=None):
        pass

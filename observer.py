__author__ = 'Robert W. Curtiss'
__project__ = 'OScope'

"""
====================================================
Author: Robert W. Curtiss
    Project: OScope
    File: observer_pattern
    Created: Jan, 08, 2021
    
    Description:
    
===================================================
"""


class Observer:
    def update(selfself, obj, *args, **kwargs):
        raise NotImplementedError


class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

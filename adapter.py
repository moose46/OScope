__author__ = 'Robert W. Curtiss'
__project__ = 'OScope'

"""
====================================================
Author: Robert W. Curtiss
    Project: OScope
    File: adapter
    Created: Jan, 08, 2021
    
    Description:
    
===================================================
"""


class Scope():
    print('Calling Scope')


class Multimeter():
    print('Calling MultiMeter')


class FileTypeAdapter:
    _initialised = False

    def __init__(self, fileType, **adapter_methods):
        self.fileTypes = fileType

        for key, value in adapter_methods.items():
            func = getattr(self.fileTypes, value)
            self.__setattr__(key, func)
        self._initialised = True

    def __getattr__(self, attr):
        return getattr(self.fileTypes, attr)

    def __setattr__(self, key, value):
        """Set attributes normally during initialisation"""
        if not self._initialised:
            super().__setattr__(key, value)
        else:
            """Set attributes on fileTypeFunction after initialisation"""
            setattr(self.fileTypes, key, value)

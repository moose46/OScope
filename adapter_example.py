__author__ = 'Robert W. Curtiss'
__project__ = 'OScope'

"""
====================================================
Author: Robert W. Curtiss
    Project: OScope
    File: adapter_example
    Created: Jan, 10, 2021
    
    Description:
    
===================================================
"""


class EuropeanSocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

    def earth(self): pass


# Adaptee
class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# Target interface
class USASocketInterface:

    def voltage(self): return 999

    def live(self): pass

    def neutral(self): pass


# The Adapter
class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return self.__socket.voltage()

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


# Client
class ElectricKettle:
    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle on fire!")
        else:
            if self.__power.live() == 1 and \
                    self.__power.neutral() == -1:
                print("Coffee time!")
            else:
                print("No power.")


def main():
    # Plug in
    socket = Socket()
    print(socket.voltage())
    adapter = Adapter(socket)
    print(socket.live())
    print(adapter.voltage())
    kettle = ElectricKettle(adapter)

    # Make coffee
    kettle.boil()

    return 0


if __name__ == "__main__":
    main()

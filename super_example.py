__author__ = 'Robert W. Curtiss'
__project__ = 'OScope'

"""
====================================================
Author: Robert W. Curtiss
    Project: OScope
    File: super_example
    Created: Jan, 09, 2021
    
    Description:
    
===================================================
"""


class minniMe:
    print("Hello from Minni Me")


class minniMe2:
    print("Hello from Minni Me2")


class Me:
    # this class sets an attribute for a string and a function
    def __init__(self):
        super(Me, self).__init__()
        super(Me, self).__setattr__("moose", "poop")
        super(Me, self).__getattribute__("moose")
        # this works
        super(Me, self).__setattr__('func', minniMe())
        super(Me, self).__getattribute__('func')
        # this does not work
        # self.func2 = miniMe()


x = Me()
print(x.__getattribute__("moose"))
x.func

#    Set a named attribute on an object; setattr(x, 'y', v) is equivalent to
#    ``x.y = v''.
setattr(x, 'func2', minniMe2())

x.func2

x.y = "squirrel"

print(x.y)

"""
This week I want you to make a class that represents a circle.
The circle should have a radius, a diameter, and an area. It should also have a nice string representation.
"""

import math

class Circle():

    def __init__(self, radius = 1):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    
    # string representation on terminal
    def __repr__(self):
        return 'Circle({})'.format(self.radius)
    
    # @property decorator makes a method behave like an attribute when set
    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    # @<property>.setter decorator allow us to auto-update other attributes when setting <property>
    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            raise ValueError("Diameter cannot be negative")
        self.radius = diameter / 2

    # what was missed by me
    #For this we need to make a setter for our diameter property. Here are just the diameter property methods in our class:
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

  



a = Circle(radius=5)
print(a)
print(a.diameter)
print(a.area)
a.radius = 1
print(a.diameter)
print(a.area)

a.diameter = 4
print(a.radius)
#a.area = 3

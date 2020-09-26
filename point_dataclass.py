"""
Point solution as a dataclass 
We've removed our __init__, __repr__, and __eq__ methods here and replaced them with type hints for x, y, and z. 
That dataclass class decorator will automatically create an initializer, string representation, and comparison methods for us based on those type hints.
The only other thing we've changed here is that our __iter__ method uses the astuple helper which takes a data class and returns a tuple of its values.
"""


from dataclasses import astuple, dataclass


@dataclass
class Point:

    """Three-dimensional point."""

    x: float
    y: float
    z: float

    def __add__(self, other):
        """Return copy of our point, shifted by other."""
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1+x2, y1+y2, z1+z2)

    def __sub__(self, other):
        """Return copy of our point, shifted by other."""
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1-x2, y1-y2, z1-z2)

    def __mul__(self, scalar):
        """Return new copy of our point, scaled by given value."""
        x, y, z = self
        return Point(scalar*x, scalar*y, scalar*z)

    __rmul__ = __mul__

    def __iter__(self):
        yield from astuple(self)
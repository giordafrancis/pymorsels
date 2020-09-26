"""
Python Morsel
Define a three dimensional point:
topics covered:
- string repr
- comparison and order __eq__
    https://treyhunner.com/2019/03/python-deep-comparisons-and-code-readability/#Deep_equality
- __add__ and __sub__
- __mul__ and __rmul__ for cummutative operation right multiplication
- __iter__ to assign tuple unpacking to an object yield from to yeld from an iterable
    because iter was assigned to class, we can refactor methods using tuple unpacking
    https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/

- check alternative data class solutions
    point_dataclass.py off the shelf __init__, __eq__ and __repr__
    https://www.youtube.com/watch?v=vD1KZgHCNCs&feature=youtu.be


"""

class Point(object):
    """
    Define a three dimensional Point
    """
    def __init__(self, x: int, y: int, z: int):
        self.x , self.y, self.z =  x, y, z
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 + x2, y1 + y2, z1 + z2)
    
    def __sub__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, num: int):
        x, y, z = self
        return Point(x * num, y * num, z * num)

    def __rmul__(self, num: int):
        return self.__mul__(num)

    def __iter__(self):
        yield from (self.x, self.y, self.z)

print(Point(1,2,3))
assert Point(1,2,3) == Point(1, 2, 3)
assert (Point(1,1,1) + Point(1,1,1)) == Point(2,2,2)
assert (Point(1,1,1) - Point(1,1,1)) == Point(0,0,0)
assert (Point(1,1,1) * 0 ) == Point(0,0,0)
assert (0 * Point(1,1,1)) == Point(0,0,0)
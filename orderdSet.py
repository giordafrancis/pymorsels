"""Ordered set
When making a data structure that closely resembles one of Python's built-in data structures, consider inheriting from one of the abstract base classes in collections.abc.
https://stackoverflow.com/questions/5359679/python-class-accessible-by-iterator-and-index/27803404#27803404
"""

from collections.abc import MutableSet , Sequence
#from collections import deque this works but fails memory efficiency test

class OrderedSet(MutableSet, Sequence):

    def __init__(self, iterable):
        self.dict = dict.fromkeys(iterable, None)
    #def __iter__(self): no longer needed inherits from abc Sequence
        #yield from self.dict.keys() 
    def __len__(self):
        return len(self.dict)
    def __contains__(self, value):
        return value in self.dict
    def __getitem__(self, index):
        return list(self.dict.keys())[index]

    def __eq__(self, other):
        # copied from solutions 
        # check for same len and if all itmes are the same
        # inheritance to Mutable set allows yo to use type below. 
        if isinstance(other, type(self)):
            return (
                len(self) == len(other) and
                all(x == y for x, y in zip(self, other))
            )
        return super().__eq__(other)



    def add(self, key):
        self.dict[key] = None
    def discard(self, key):
        self.dict.pop(key, None) # None handles key error


words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
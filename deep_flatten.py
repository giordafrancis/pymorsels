""" deep flatten notes
The isinstance function accepts an object and a tuple of types and will return True if that object's class inherits from any of those types.
(ie named tuple) best to use instead of type checking
As we dont know what is the depth of the list this problem lends to a recursivve solution
"""

import collections
from typing import Iterable, Union

def deep_flatten(input: Iterable) -> Iterable[Union[int,str]]:

    for item in input:
        if isinstance(item, collections.abc.Iterable) and not isinstance(item, (str, bytes)):
            yield from deep_flatten(item)
        else:
            yield item


assert list(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])) == [1, 2, 3, 4, 5, 6, 7, 8]
assert list(deep_flatten([[1, [2, 3]], 4, 5])) == [1, 2, 3, 4, 5]#
assert list(deep_flatten([['apple', 'pickle'], ['pear', 'avocado']])) == ['apple', 'pickle', 'pear', 'avocado']

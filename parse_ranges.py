"""
Parse ranges 
my favorite Trey Hunner approach below
Whenever you see "for x in iterable: yield x" you can instead write "yield from iterable".
"""

from typing import List, Iterable
from itertools import chain

def start_stop(ranges: str) -> Iterable:
    ranges = ranges.replace("->exit","")
    iterable = (
        chunk.split('-')
        for chunk in ranges.split(',')
    )
    for arange in iterable:
        if len(arange) == 1:
            yield range(int(*arange), int(*arange) + 1)
            continue
        start, stop = arange
        yield range(int(start ), int(stop)+ 1)

def parse_ranges(ranges: str)-> List[int]:

    iterable = start_stop(ranges)
    return chain.from_iterable(iterable)


def parse_ranges(ranges):
    for group in ranges.split(','):
        start, sep, end = group.partition('-')
        if end.startswith('>') or not sep:
            yield int(start)
        else:
            yield from range(int(start), int(end)+1)

# base case
#assert parse_ranges('1-2,4-4,8-10') == [1, 2, 4, 8, 9, 10]
#assert parse_ranges('0-0, 4-8, 20-20, 43-45') == [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]



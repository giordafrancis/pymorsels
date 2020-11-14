"""
context manager
"""

from contextlib import contextmanager

@contextmanager
def supress(*args):
    try:
        yield
    except args:
        pass
                  
        
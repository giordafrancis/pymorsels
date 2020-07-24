"""
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.
"""


from typing import List, Optional
Matrix = List[List[int]]


def add(matrix1: Matrix, matrix2:Matrix) -> Matrix:
    outer_list = []
    for m1, m2 in zip(matrix1, matrix2):
        inner_list = []
        for val1, val2 in zip(m1, m2):
            inner_list.append(val1 + val2)
        outer_list.append(inner_list)
    return outer_list

def add2(*matrices) -> Matrix:
    outer_list = []
    for ms in zip(*matrices):
        inner_list = []
        for values in zip(*ms):
            inner_list.append(sum(values))
        outer_list.append(inner_list)
    return outer_list

def add3(*matrices) -> Matrix:

    if not raise_exception(*matrices):
        raise ValueError("not all inner lists are the same length")
    
    outer_list = []
    for ms in zip(*matrices):
        inner_list = [sum(values)
                      for values in zip(*ms)
                     ]
        outer_list.append(inner_list)
    return outer_list

def raise_exception(*matrices)-> bool:
    lst = {len(lst)
            for m in matrices 
            for lst in m}
    
    num_lst  = {len(m) for m in matrices}
    
    return len(lst) == len(num_lst)

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

assert add(matrix1, matrix2) == [[3, -3], [-3, 3]]

matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]

assert add2(matrix1, matrix2, matrix3) == [[8, 8], [7, 7]]
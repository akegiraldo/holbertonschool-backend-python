#!/usr/bin/env python
from typing import List

"""Complex types - list of floats"""


def sum_list(input_list: List[float]) -> float:
    """
    Function which takes a list input_list of
    floats as argument and returns their sum
    as a float
    """
    result: float = 0
    for num in input_list:
        result += num
    return result

#!/usr/bin/env python
from typing import List, Union

"""Complex types - mixed list"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function which takes a list mxd_lst of integers and floats
    and returns their sum as a float
    """
    result: float = 0
    for num in mxd_lst:
        result += num
    return result

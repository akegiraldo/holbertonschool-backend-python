#!/usr/bin/env python3
"""Type Checking"""

from typing import List, Any, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Function validated by mypy"""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)

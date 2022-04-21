#!/usr/bin/env python3
"""Let's duck type an iterable object"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that receives a list of str, and returns a list of
    tuples, where the first position is the str and the second
    position is the size of str
    """
    return [(i, len(i)) for i in lst]

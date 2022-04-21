#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""

from typing import Optional, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Function that receives a list of any type, and returns the value of
    the first position, or none if list is null or empty
    """
    if lst:
        return lst[0]
    else:
        return None

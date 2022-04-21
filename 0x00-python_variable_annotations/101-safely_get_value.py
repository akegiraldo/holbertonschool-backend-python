#!/usr/bin/env python3
"""More involved type annotations"""

from typing import Mapping, Any, Optional, TypeVar, Union


def safely_get_value(
            dct: Mapping,
            key: Any,
            default: Optional[TypeVar('T')] = None
        ) -> Union[Any, TypeVar('T')]:
    """
    Function that receives a dictionary, a
    key, and a default value, and must
    return the dictionary value at the given
    key position. In case it does not exist,
    return the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default

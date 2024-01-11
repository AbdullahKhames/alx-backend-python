#!/usr/bin/env python3
"""
module to demonstrate type var
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """
    safely_get_value
    :param dct: dct Mapping
    :param key: key
    :param default: def
    :return: val
    """
    if key in dct:
        return dct[key]
    else:
        return default

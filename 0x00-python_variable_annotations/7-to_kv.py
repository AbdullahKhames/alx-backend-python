#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple
"""
import math
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv converts str to tuple
    :param k: string to be converted
    :param v: int or float to be squared
    :return: tuple
    """
    tup = (k, math.pow(v, 2))
    return tup

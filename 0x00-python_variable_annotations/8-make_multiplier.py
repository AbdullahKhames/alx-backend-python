#!/usr/bin/env python3
"""8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that returns a multiplier function
    :param multiplier: the multiplier to set iin the multiplier funstion
    :return: function that multiplies a float
    """
    fun: Callable[[float], float] = lambda x: x * multiplier
    return fun

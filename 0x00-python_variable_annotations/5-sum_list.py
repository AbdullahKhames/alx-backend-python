#!/usr/bin/env python3
"""module for complex types"""
import functools
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    list sum
    :param input_list: list of loats to be added
    :return: sum product
    """
    return functools.reduce(lambda a, b: a + b, input_list)

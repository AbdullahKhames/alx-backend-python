#!/usr/bin/env python3
"""sum_mixed_list  module"""
import functools
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list for adding a mixed list
    :param mxd_lst: the list to be added
    :return: sum product
    """
    return functools.reduce(lambda a, b: a + b, mxd_lst)

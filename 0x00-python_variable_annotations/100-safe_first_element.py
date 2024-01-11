#!/usr/bin/env python3
"""
module to safe type this function
"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element
    :param lst:  Sequence[Any]
    :return: Union[Any, None]
    """
    if lst:
        return lst[0]
    else:
        return None

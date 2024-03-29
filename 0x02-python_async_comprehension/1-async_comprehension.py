#!/usr/bin/env python3
"""module to test async comprehension
"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function that test async comprehension
    """
    return [i async for i in async_generator()]

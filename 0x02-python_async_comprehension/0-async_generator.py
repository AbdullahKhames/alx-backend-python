#!/usr/bin/env python3
"""module to test async comprehension
"""
import random
import asyncio


async def async_generator() -> float:
    """function that test async comprehension
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3
"""module to test async comprehension
"""
import typing
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function that test async comprehension
    """
    start = time()
    await asyncio.gather(asyncio.create_task(async_comprehension()),
                         asyncio.create_task(async_comprehension()),
                         asyncio.create_task(async_comprehension()),
                         asyncio.create_task(async_comprehension()))
    end = time()

    return (end - start)

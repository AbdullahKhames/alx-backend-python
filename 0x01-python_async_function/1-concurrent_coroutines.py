#!/usr/bin/env python3
"""module to test basic async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """function to test async operations
    """
    delays: List[float] = []
    futures = []
    for _ in range(n):
        futures.append(wait_random(max_delay))
    for future in asyncio.as_completed(futures):
        delay = await future
        delays.append(delay)
    return delays

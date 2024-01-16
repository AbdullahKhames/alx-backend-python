#!/usr/bin/env python3
"""module to test basic async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function to test async operations
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    delays = await asyncio.gather(*tasks)

    return delays

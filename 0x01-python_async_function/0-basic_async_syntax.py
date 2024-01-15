#!/usr/bin/env python3
"""module to test basic async
"""
import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    """function to test async operations
    max_delay: maximum delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

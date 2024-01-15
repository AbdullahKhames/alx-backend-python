#!/usr/bin/env python3
"""module to test basic async
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function to test async operations
    """
    before = time.time()
    asyncio.run(wait_n(n, max_delay))
    after = time.time()
    total_time = after - before
    return total_time / n

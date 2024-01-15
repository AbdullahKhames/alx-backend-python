#!/usr/bin/env python3
"""module to test basic async
"""
import random


async def wait_random(max_delay=10):
    """function to test async operations
    max_delay: maximum delay
    """
    return random.uniform(0, max_delay)


if __name__ == "__main__":
    pass

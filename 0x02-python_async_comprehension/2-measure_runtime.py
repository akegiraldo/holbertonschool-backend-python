#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that will execute
    async_comprehension four times
    in parallel using asyncio.gather.
    Measure_runtime should measure
    the total runtime and return it
    """
    current_time: float = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(0, 4)])
    elapsed_time: float = time.time() - current_time
    return elapsed_time

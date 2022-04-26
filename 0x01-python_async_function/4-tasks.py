#!/usr/bin/env python3
"""4. Tasks"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The code is nearly identical to wait_n except
    task_wait_random is being called
    """
    result: List[float] = []

    tasks: List[asyncio.Task] = [task_wait_random(max_delay)
                                 for _ in range(0, n)]

    for coro in asyncio.as_completed(tasks):
        result.append(await coro)

    return result

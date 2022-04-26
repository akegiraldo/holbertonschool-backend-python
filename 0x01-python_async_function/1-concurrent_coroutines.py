#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""

import asyncio
from types import coroutine
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine called wait_n that
    takes in 2 int arguments (in this
    order): n and max_delay. You will
    spawn wait_random n times with the
    specified max_delay.

    Wait_n should return the list of
    all the delays (float values). The
    list of the delays should be in
    ascending order without using sort()
    because of concurrency
    """
    result: List[float] = []

    coroutines: List[coroutine] = [wait_random(max_delay) for _ in range(0, n)]

    for coro in asyncio.as_completed(coroutines):
        result.append(await coro)

    return result

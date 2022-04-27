#!/usr/bin/env python3
"""0. Async Generator"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine will loop 10
    times, each time
    asynchronously wait 1
    second, then yield a
    random number between
    0 and 10. Use the random
    module
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

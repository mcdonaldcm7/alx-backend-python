#!/usr/bin/env python3
"""
Task

0. Async Generator
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then
yield a random number between 0 and 10. Use the random module.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    Return a random number between 0 and 10, 10 times with a second delay
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

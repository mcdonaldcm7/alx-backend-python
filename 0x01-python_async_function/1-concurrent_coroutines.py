#!/usr/bin/env python3
"""
Task

1. Let's execute multiple coroutines at the same time with async

Import wait_random from the previous python file that you’ve written and write
an async routine called wait_n that takes in 2 int arguments (in this order): n
and max_delay. You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of the
delays should be in ascending order without using sort() because of concurrency
"""
import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Returns an ordered list of time the coroutines returned after being called
    n times with max_delay
    """
    coroutines = []
    async with asyncio.TaskGroup() as tg:
        for _ in range(n):
            coroutines.append(tg.create_task(wait_random(max_delay)))

    results = []
    for coroutine in asyncio.as_completed(coroutines):
        earliest_result = await coroutine
        results.append(earliest_result)
    results = await asyncio.gather(*coroutines)
    return results

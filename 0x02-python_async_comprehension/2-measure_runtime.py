#!/usr/bin/env python3
"""
Task

2. Run time for four parallel comprehensions
Import `async_comprehension` from the previous file and write a
`measure_runtime` coroutine that will execute `async_comprehension` four times
in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of four parallel `async_comprehension` and returns it
    """
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension()
                         )
    return (time.perf_counter() - s)

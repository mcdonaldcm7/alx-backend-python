#!/usr/bin/env python3
"""
Task

4. Tasks
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]

    results = await asyncio.gather(*coroutines)

    # Manual sorting (Bubble Sort)
    for i in range(len(results)):
        for j in range(0, len(results) - i - 1):
            if results[j] > results[j + 1]:
                results[j], results[j + 1] = results[j + 1], results[j]
    return results

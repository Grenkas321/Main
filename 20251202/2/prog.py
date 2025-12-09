import asyncio
import random
import sys

async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    if middle < finish:
        await event_in2.wait()
    i = start
    j = middle
    ind = start
    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            A2[ind] = A1[i]
            i += 1
        else:
            A2[ind] = A1[j]
            j += 1
        ind += 1

    while i < middle:
        A2[ind] = A1[i]
        i += 1
        ind += 1

    while j < finish:
        A2[ind] = A1[j]
        j += 1
        ind += 1
    event_out.set()

async def mtasks(A):
    tasks = []
    events = [asyncio.Event() for i in range(len(A))]
    for i in events: i.set()
    step = 1
    B = [None for i in range(len(A))]
    cur = A[:]
    nxt = B
    length = len(A)
    while step < length:
        start = 0
        events_out = []
        while start < length:
            middle = min(start + step, length)
            finish = min(start + 2 * step, length)
            event_in1 = events[start // step]
            if middle < length: event_in2 = events[middle // step]
            else: event_in2 = asyncio.Event()
            event_out = asyncio.Event()
            tasks.append(asyncio.create_task(merge(cur, nxt, start, middle, finish, event_in1, event_in2, event_out)))
            start += 2 * step
            events_out.append(event_out)
        cur, nxt = nxt, cur
        step *= 2
        events = events_out
    return tasks, cur

exec(sys.stdin.read())

import asyncio
import random
import sys

async def merge(A1, A2, start, middle, finish,
                event_in1: asyncio.Event,
                event_in2: asyncio.Event,
                event_out: asyncio.Event):
    await event_in1.wait()
    await event_in2.wait()

    i, j, k = start, middle, start

    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]
            i += 1
        else:
            A2[k] = A1[j]
            j += 1
        k += 1

    while i < middle:
        A2[k] = A1[i]
        i += 1
        k += 1

    while j < finish:
        A2[k] = A1[j]
        j += 1
        k += 1

    event_out.set()


async def mtasks(A):
    n = len(A)
    A1 = list(A)
    B = [0] * n
    tasks = []

    if n == 0:
        return tasks, B

    width = 1
    src = A1
    dst = B

    seg_count = (n + width - 1) // width
    events_src = [asyncio.Event() for _ in range(seg_count)]
    for ev in events_src:
        ev.set()

    while width < n:
        seg_next_count = (n + 2 * width - 1) // (2 * width)
        events_next = [asyncio.Event() for _ in range(seg_next_count)]

        for pair_idx in range(seg_next_count):
            left_seg = 2 * pair_idx
            right_seg = left_seg + 1

            event_in1 = events_src[left_seg]

            if right_seg < seg_count:
                event_in2 = events_src[right_seg]
            else:
                event_in2 = asyncio.Event()
                event_in2.set()

            start = left_seg * width
            middle = min(start + width, n)
            finish = min(start + 2 * width, n)

            tasks.append(
                merge(
                    src, dst,
                    start, middle, finish,
                    event_in1, event_in2,
                    events_next[pair_idx],
                )
            )

        width *= 2
        src, dst = dst, src
        seg_count = seg_next_count
        events_src = events_next

    return tasks, src

exec(sys.stdin.read())
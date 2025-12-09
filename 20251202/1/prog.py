import asyncio
import random

async def writer(queue: asyncio.Queue, delay: int, stop_event: asyncio.Event):
    i = 0
    while True:
        try:
            await asyncio.wait_for(stop_event.wait(), timeout=delay)
            break
        except asyncio.TimeoutError:
            await queue.put(f"{i}_{delay}")
            i += 1


async def stacker(queue: asyncio.Queue, stack: asyncio.LifoQueue, stop_event: asyncio.Event):
    while True:
        get_task = asyncio.create_task(queue.get())
        stop_task = asyncio.create_task(stop_event.wait())

        done, pending = await asyncio.wait(
            {get_task, stop_task},
            return_when=asyncio.FIRST_COMPLETED,
        )

        if stop_task in done:
            get_task.cancel()
            break
        else:
            stop_task.cancel()
            item = get_task.result()
            await stack.put(item)


async def reader(stack: asyncio.LifoQueue, count: int, delay: int, stop_event: asyncio.Event):
    for _ in range(count):
        await asyncio.sleep(delay)
        value = await stack.get()
        print(value)
    stop_event.set()


async def main():
    data = input().strip()
    if not data:
        return

    d1, d2, d3, count = map(int, data.split(','))

    queue = asyncio.Queue()
    stack = asyncio.LifoQueue()
    stop_event = asyncio.Event()

    tasks = [
        writer(queue, d1, stop_event),
        writer(queue, d2, stop_event),
        stacker(queue, stack, stop_event),
        reader(stack, count, d3, stop_event),
    ]

    await asyncio.gather(*tasks)



asyncio.run(main())


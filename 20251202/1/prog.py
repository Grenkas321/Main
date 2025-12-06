import asyncio

event = asyncio.Event()
async def writer(queue, delay):
    i = 0
    while not event.is_set():
        await asyncio.sleep(delay)
        await queue.put(f'{i}_{delay}')
        i += 1

async def stacker(queue, stack):
    while not event.is_set():
        el = await queue.get()
        await stack.put(el)

async def reader(stack, num, delay):
    for i in range(num):
        await asyncio.sleep(delay)
        el = await stack.get()
        print(el)
    event.set()

async def main():
    delay1, delay2, delay3, num = eval(input())
    queue = asyncio.Queue()
    stack = asyncio.Queue()
    await asyncio.gather(reader(stack, num, delay3), writer(queue, delay1), writer(queue, delay2), stacker(queue, stack))

asyncio.run(main())
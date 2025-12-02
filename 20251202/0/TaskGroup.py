import asyncio

async def squarer(x: float) -> float:
    return x * x

async def doubler(x: float) -> float:
    return 2 * x

async def main():
    vals = [3, 5]

    sq = [None, None]
    async with asyncio.TaskGroup() as tg:
        tg.create_task(_store(squarer(vals[0]), sq, 0))
        tg.create_task(_store(squarer(vals[1]), sq, 1))

    res = [None, None]
    async with asyncio.TaskGroup() as tg:
        tg.create_task(_store(doubler(sq[0]), res, 0))
        tg.create_task(_store(doubler(sq[1]), res, 1))

    print(res)

async def _store(coro, container, idx):
    container[idx] = await coro

asyncio.run(main())

import asyncio

async def squarer(x: float) -> float:
    return x * x

async def doubler(x: float) -> float:
    return 2 * x

async def main():
    vals = [3, 5]

    sq = await asyncio.gather(
        squarer(vals[0]),
        squarer(vals[1])
    )

    res = await asyncio.gather(
        doubler(sq[0]),
        doubler(sq[1])
    )

    print(res)


asyncio.run(main())



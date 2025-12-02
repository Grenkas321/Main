import asyncio

async def prod(q1: asyncio.Queue):
    for i in range(5):
        value = f"value_{i}"
        await q1.put(value)
        print(f"prod: put {value} to q1")
        await asyncio.sleep(1)
    await q1.put(None)
    print("prod: put None to q1 (done)")

async def mid(q1: asyncio.Queue, q2: asyncio.Queue):
    while True:
        value = await q1.get()
        print(f"mid: got {value} from q1")
        if value is None:
            await q2.put(None)
            print("mid: put None to q2 (done)")
            break
        await q2.put(value)
        print(f"mid: put {value} to q2")

async def cons(q2: asyncio.Queue):
    while True:
        value = await q2.get()
        print(f"cons: got {value} from q2")
        if value is None:
            print("cons: done")
            break

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()

    t_prod = asyncio.create_task(prod(q1))
    t_mid = asyncio.create_task(mid(q1, q2))
    t_cons = asyncio.create_task(cons(q2))

    await asyncio.gather(t_prod, t_mid, t_cons)


asyncio.run(main())

import asyncio

async def snd(evsnd: asyncio.Event):
    evsnd.set()
    print("snd: generated evsnd")

async def mid(k: int, evsnd: asyncio.Event, evmid: asyncio.Event):
    await evsnd.wait()
    print(f"mid{k}: received evsnd")
    evmid.set()
    print(f"mid{k}: generated evmid{k}")

async def rcv(evmid0: asyncio.Event, evmid1: asyncio.Event):
    await evmid0.wait()
    print("rcv: received evmid0")
    await evmid1.wait()
    print("rcv: received evmid1")

async def main():
    evsnd = asyncio.Event()
    evmid0 = asyncio.Event()
    evmid1 = asyncio.Event()

    t_rcv = asyncio.create_task(rcv(evmid0, evmid1))
    t_mid1 = asyncio.create_task(mid(1, evsnd, evmid1))
    t_mid0 = asyncio.create_task(mid(0, evsnd, evmid0))
    t_snd = asyncio.create_task(snd(evsnd))

    await asyncio.gather(t_rcv, t_mid0, t_mid1, t_snd)

asyncio.run(main())

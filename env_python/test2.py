from quart import Quart
import asyncio
# async io
# cpu 작업과 i/o 작업 병렬


async def add(a, b):
    await asyncio.sleep(1)
    print(f"a+b={a+b}")
    return a+b


async def tmp():
    print("hello world")
    res = await add(10, 20)
    await asyncio.sleep(10)
    print("add result ", res)


async def printHello3Sec():
    while True:
        await asyncio.sleep(3)
        print("hello 3sec")


async def printHello5sec():
    while True:
        await asyncio.sleep(5)
        print("hello 5sec")


async def main():
    futures = [
        asyncio.ensure_future(printHello3Sec()),
        asyncio.ensure_future(printHello5sec())]
    await asyncio.gather(*futures)
    return

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()

app = Quart(__name__)


if __name__ == "__main__":
    asyncio.run(app.run_task())

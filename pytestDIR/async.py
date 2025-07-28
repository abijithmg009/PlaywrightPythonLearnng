import asyncio


async def task(name):
    print(f"Starting {name}")
    await asyncio.sleep(2)
    print(f"Finishing {name}")

async def main():
    await asyncio.gather(task("Abijith"), task("MG"))


asyncio.run(main())
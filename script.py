import asyncio
import time

async def async_task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} completed after {delay} seconds")
    return f"Result from {name}"

async def main():
    tasks = [
        async_task("A", 2),
        async_task("B", 3),
        async_task("C", 1)
    ]
    results = await asyncio.gather(*tasks)
    print("All tasks completed:", results)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print("Total execution time:", time.time() - start_time, "seconds")

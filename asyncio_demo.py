# Modern versions of Python have support for "asynchronous code" using something called "coroutines", with async and await syntax.

import asyncio
import time

async def say_after(delay, what):
    """An asynchronous coroutine that waits a specified delay and then prints a message."""
    await asyncio.sleep(delay) # Pauses this coroutine, but allows other tasks to run
    print(what)

async def main():
    """The main asynchronous function that sets up and runs the tasks concurrently."""
    print(f"started at {time.strftime('%X')}")

    # Create tasks to run say_after concurrently
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    # Wait until both tasks are completed (should take only about 2 seconds, not 3)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

# Run the main function using the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())

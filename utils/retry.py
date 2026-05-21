import asyncio

async def retry_task(func, retries=3):

    for attempt in range(retries):

        try:
            return func()

        except Exception as e:

            print(f"Retry {attempt+1}")

            await asyncio.sleep(2)

    raise Exception("Task Failed")
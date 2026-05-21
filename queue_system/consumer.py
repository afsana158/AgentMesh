import redis
import json
import time
import asyncio

from agents.retriever import retriever_agent
from agents.analyzer import analyzer_agent
from agents.writer import writer_agent

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


async def process_task(task):

    print(f"\nProcessing Task: {task}")

    retrieved = retriever_agent(task)
    print("Retriever Agent Done")

    await asyncio.sleep(1)

    analyzed = analyzer_agent(retrieved)
    print("Analyzer Agent Done")

    await asyncio.sleep(1)

    final = writer_agent(analyzed)
    print("Writer Agent Done")

    print("\nFINAL OUTPUT:")
    print(final)


async def consumer():

    while True:

        task_data = r.lpop("agent_queue")

        if task_data:

            task_json = json.loads(task_data)

            try:
                await process_task(task_json["task"])

            except Exception as e:

                print("Task Failed:", e)

                r.rpush("agent_queue", json.dumps(task_json))

        await asyncio.sleep(1)


asyncio.run(c
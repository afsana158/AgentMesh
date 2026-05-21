import redis
import json
import asyncio

from AgentMesh.queue_system.pubsub import publish_log
from AgentMesh.agents.writer import writer_agent

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

async def consumer():

    while True:

        task_data = r.lpop("writer_queue")

        if task_data:

            task = json.loads(task_data)

            try:

                # STREAM LIVE LOGS
                publish_log("Writer Agent Processing...")
                publish_log(task["task"])

                # Run writer agent
                result = writer_agent(task["task"])

                publish_log("Writer Completed")

                publish_log("FINAL OUTPUT:")
                publish_log(result)

            except Exception as e:

                publish_log(f"Writer Failed: {e}")

                # Retry failed task
                r.rpush("writer_queue", task_data)

        await asyncio.sleep(1)

asyncio.run(consumer())
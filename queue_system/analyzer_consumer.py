import redis
import json
import asyncio

from queue_system.pubsub import publish_log
from agents.analyzer import analyzer_agent

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

async def consumer():

    while True:

        task_data = r.lpop("analyzer_queue")

        if task_data:

            task = json.loads(task_data)

            try:

                # STREAM LIVE LOGS
                publish_log("Analyzer Agent Processing...")
                publish_log(task["task"])

                # Run analyzer agent
                result = analyzer_agent(task["task"])

                publish_log("Analyzer Completed")

                # Send to writer queue
                r.rpush(
                    "writer_queue",
                    json.dumps({
                        "task": result
                    })
                )

                publish_log("Sent To Writer Queue")

            except Exception as e:

                publish_log(f"Analyzer Failed: {e}")

                # Retry failed task
                r.rpush("analyzer_queue", task_data)

        await asyncio.sleep(1)

asyncio.run(consumer())
import redis
import json
import asyncio

from AgentMesh.queue_system.pubsub import publish_log
from AgentMesh.agents.retriever import retriever_agent

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

async def consumer():

    while True:

        task_data = r.lpop("retriever_queue")

        if task_data:

            task = json.loads(task_data)

            try:

                # STREAM LIVE LOGS
                publish_log("Retriever Agent Processing...")
                publish_log(task["task"])

                # Run retriever agent
                result = retriever_agent(task["task"])

                publish_log("Retriever Completed")

                # Send to analyzer queue
                r.rpush(
                    "analyzer_queue",
                    json.dumps({
                        "task": result
                    })
                )

                publish_log("Sent To Analyzer Queue")

            except Exception as e:

                publish_log(f"Retriever Failed: {e}")

                # Retry failed task
                r.rpush("retriever_queue", task_data)

        await asyncio.sleep(1)

asyncio.run(consumer())
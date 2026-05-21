import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

async def publish_task(task):

    r.rpush("agent_queue", json.dumps({
        "task": task,
        "status": "pending"
    }))
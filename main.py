from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import redis
import json
import asyncio

from agents.planner import planner_agent
    
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

@app.get("/")
def home():
    return {"message": "Agentic AI System Running"}

@app.post("/process")
async def process_query(query: str):

    async def event_stream():

        pubsub = r.pubsub()
        pubsub.subscribe("agent_logs")

        yield "Planner Agent Started...\n"

        tasks = await planner_agent(query)

        yield f"Tasks Created: {tasks}\n"

        for task in tasks:

            r.rpush(
                "retriever_queue",
                json.dumps({
                    "task": task
                })
            )

            yield f"Task Sent: {task}\n"

        yield "Pipeline Started...\n\n"

        while True:

            message = pubsub.get_message()

            if message and message["type"] == "message":

                yield f"{message['data']}\n"

            await asyncio.sleep(0.5)

    return StreamingResponse(
        event_stream(),
        media_type="text/plain"
    )
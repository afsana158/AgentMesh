import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

CHANNEL = "agent_logs"

def publish_log(message):

    r.publish(CHANNEL, message)
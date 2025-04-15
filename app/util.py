import redis
import uuid
import json

# Redis client
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def create_session_id():
    return str(uuid.uuid4())

def save_history(session_id, history):
    r.set(session_id, json.dumps(history))

def get_history(session_id):
    data = r.get(session_id)
    return json.loads(data) if data else []

def delete_session(session_id):
    r.delete(session_id)

import os

import psycopg
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    text: str


def connect():
    return psycopg.connect(os.environ["DATABASE_URL"])


@app.get("/")
def hello():
    return {"message": "Hello, Docker!"}


@app.post("/messages")
def add_message(message: Message):
    with connect() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS messages (text TEXT NOT NULL)")
        conn.execute("INSERT INTO messages (text) VALUES (%s)", (message.text,))
    return message


@app.get("/messages")
def list_messages():
    with connect() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS messages (text TEXT NOT NULL)")
        return {"messages": [row[0] for row in conn.execute("SELECT text FROM messages")]}

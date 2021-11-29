from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/demo")
async def root():
    hostname = socket.gethostname()
    return {"message": f"I AM FROM {hostname}"}


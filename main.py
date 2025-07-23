from fastapi import FastAPI #type: ignore

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello FastAPI!"}

@app.get("/hello")
async def hello_world():
    return {"message": "Hello World!"}
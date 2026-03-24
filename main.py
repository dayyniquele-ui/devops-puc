from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/teste1")
async def root():
    return {"message": "Hello World"}

@app.get ("/teste")
async def funcaoteste():
    return {"teste": "deu certo"}

@app.get ("/teste2")
async def funcaoteste2 ():
    return {"teste1" : True, "num_aleatorio": random.randint (a=0, b=100)}

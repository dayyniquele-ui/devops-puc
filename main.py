from fastapi import FastAPI
import random
from pydantic import BaseModel

class Estudante(BaseModel):
    id: int
    nome: str
    curso: str
    idade: int


app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get ("/teste2")
async def funcaoteste2 ():
    return {"teste1" : True, "num_aleatorio": random.randint (a=0, b=100)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/atualizar/{estudante_id}")
async def update_estudante(estudante_id: int, estudante: Estudante):
    return {"estudante_id": estudante_id, "estudante": estudante}

@app.delete("/estudantes/deletar/{estudante_id}")
async def delete_estudante(estudante_id: int):
    return {"estudante_id": estudante_id, "message": "Estudante deletado com sucesso"}
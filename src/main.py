from fastapi import FastAPI
import random
from pydantic import BaseModel

class Estudante(BaseModel):
    id: int
    nome: str
    curso: str
    idade: int


app = FastAPI()

# "Banco de dados" fake
db_estudantes = {}

@app.get("/boasvindas")
async def root():
    return {"message": "Bem Vinda Dayanna"}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    db_estudantes[estudante.id] = estudante
    return estudante

@app.get("/estudantes/{estudante_id}")
async def get_estudante(estudante_id: int):
    return db_estudantes.get(estudante_id)

@app.put("/estudantes/atualizar/{estudante_id}")
async def update_estudante(estudante_id: int, estudante: Estudante):
    db_estudantes[estudante_id] = estudante
    return {"estudante_id": estudante_id, "estudante": estudante}

@app.delete("/estudantes/deletar/{estudante_id}")
async def delete_estudante(estudante_id: int):
    db_estudantes.pop(estudante_id, None)
    return {"estudante_id": estudante_id, "message": "Estudante deletado com sucesso"}
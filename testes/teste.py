from src.main import *
from unittest.mock import patch


def teste_root():
    assert root() == {"message": "Hello World"}
  
def teste_funcaoteste2 ():
    with patch('src.main.random.randint', return_value=42):
        result = funcaoteste2() 
    assert result == {"teste1": True, "num_aleatorio": 42}

def teste_create_estudante():
    estudante_teste = Estudante(id=1, nome="Dayanna", curso="ADS", idade=35)
    assert estudante_teste == create_estudante(estudante_teste)

def teste_update_estudante():
    estudante_teste = Estudante(id=1, nome="Dayanna", curso="ADS", idade=35)
    assert estudante_teste == update_estudante(1, estudante_teste)

def teste_delete_estudante():
    assert delete_estudante(1) == {"estudante_id": 1, "message": "Estudante deletado com sucesso"}


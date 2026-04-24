from src.main import *
from unittest.mock import patch


def teste_root():
    result = root()
    yield result
    assert result() == {"message": "Hello World"}
  
def teste_funcaoteste2 ():
    with patch('src.main.random.randint', return_value=42):
        result = funcaoteste2() 
        yield result
    assert result == {"teste1": True, "num_aleatorio": 42}

def teste_create_estudante():
    estudante_teste = Estudante(id=1, nome="Dayanna", curso="ADS", idade=35)
    result = create_estudante(estudante_teste)
    yield result

    assert estudante_teste == result

def teste_update_estudante():
    estudante_teste = Estudante(id=1, nome="Dayanna", curso="ADS", idade=35)
    result = update_estudante(1, estudante_teste)
    yield result
    assert estudante_teste == result

def teste_delete_estudante():
    result = delete_estudante(1)
    yield result
    assert result == {"estudante_id": 1, "message": "Estudante deletado com sucesso"}


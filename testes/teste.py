from src.main import *
from unittest.mock import patch


def test_root():
    result = root()
    assert result == {"message": "Hello World"}


def test_funcaoteste2():
    with patch('src.main.random.randint', return_value=42):
        result = funcaoteste2()
    assert result == {"teste1": True, "num_aleatorio": 42}

def test_create_estudante():
    estudante_teste = Estudante(id=1, nome="Dayanna", curso="ADS", idade=35)
    result = create_estudante(estudante_teste)
    assert estudante_teste == result

def test_update_estudante():
    estudante_teste = Estudante(id=1, nome="Dayanna", curso="ADS", idade=35)
    result = update_estudante(1, estudante_teste)
    assert estudante_teste == result

def test_delete_estudante():
    result = delete_estudante(1)
    assert result == {"estudante_id": 1, "message": "Estudante deletado com sucesso"}

import pytest
from src.main import *
from unittest.mock import patch


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_funcaoteste2():
    with patch('src.main.random.randint', return_value=42):
        result = await funcaoteste2()
    assert result == {"teste1": True, "num_aleatorio": 42}


@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(id=1, nome="Dayanna", curso="ADS", idade=35)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante():
    estudante_teste = Estudante(id=1, nome="Dayanna", curso="ADS", idade=35)
    result = await update_estudante(1, estudante_teste)

    assert result["estudante"] == estudante_teste
    assert result["estudante_id"] == 1


@pytest.mark.asyncio
async def test_delete_estudante():
    result = await delete_estudante(1)
    assert result == {"estudante_id": 1, "message": "Estudante deletado com sucesso"}
    
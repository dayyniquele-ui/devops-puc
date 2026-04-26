import pytest
from src.main import *
from unittest.mock import patch


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Bem Vinda Dayanna"}


@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(id=1, nome="Dayanna", curso="ADS", idade=35)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_get_estudante():
    estudante_teste = Estudante(id=2, nome="Ana", curso="ADS", idade=22)
    
    await create_estudante(estudante_teste)
    result = await get_estudante(2)

    assert result == estudante_teste


@pytest.mark.asyncio
async def test_get_estudante_inexistente():
    result = await get_estudante(999)
    assert result is None


@pytest.mark.asyncio
async def test_update_estudante():
    estudante_teste = Estudante(id=3, nome="João", curso="ADS", idade=30)
    
    await create_estudante(estudante_teste)

    estudante_atualizado = Estudante(id=3, nome="João Silva", curso="ADS", idade=31)
    result = await update_estudante(3, estudante_atualizado)

    assert result["estudante"] == estudante_atualizado
    assert result["estudante_id"] == 3


@pytest.mark.asyncio
async def test_delete_estudante():
    estudante_teste = Estudante(id=4, nome="Carlos", curso="ADS", idade=40)

    await create_estudante(estudante_teste)
    result = await delete_estudante(4)

    assert result == {"estudante_id": 4, "message": "Estudante deletado com sucesso"}



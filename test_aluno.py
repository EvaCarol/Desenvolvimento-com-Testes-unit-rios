import pytest
from aluno import Aluno

def test_cadastrar_nota_valida():
    aluno = Aluno()
    assert aluno.cadastrar_nota(8.5) == True
    assert len(aluno.notas) == 1

def test_cadastrar_nota_invalida():
    aluno = Aluno()
    with pytest.raises(ValueError):
        aluno.cadastrar_nota(11)
    with pytest.raises(ValueError):
        aluno.cadastrar_nota(-1)
    with pytest.raises(ValueError):
        aluno.cadastrar_nota("abc")

def test_calcular_media():
    aluno = Aluno()
    aluno.cadastrar_nota(8)
    aluno.cadastrar_nota(7)
    aluno.cadastrar_nota(9)
    assert aluno.calcular_media() == 8.0

def test_media_sem_notas():
    aluno = Aluno()
    assert aluno.calcular_media() == 0.0

def test_verificar_situacao_aprovado():
    aluno = Aluno()
    aluno.cadastrar_nota(7.5)
    aluno.cadastrar_nota(8.0)
    assert aluno.verificar_situacao() == "Aprovado"

def test_verificar_situacao_recuperacao():
    aluno = Aluno()
    aluno.cadastrar_nota(5.5)
    aluno.cadastrar_nota(6.0)
    assert aluno.verificar_situacao() == "Recuperação"

def test_verificar_situacao_reprovado():
    aluno = Aluno()
    aluno.cadastrar_nota(4.0)
    aluno.cadastrar_nota(3.5)
    assert aluno.verificar_situacao() == "Reprovado"
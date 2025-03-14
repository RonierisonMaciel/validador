from validador import validar_senha

def test_numero():
    assert not validar_senha("123")

def test_letra():
    assert not validar_senha("asd")

def test_tamanho():
    assert not validar_senha('123456')

def test_caractere_esp():
    assert not validar_senha("asd$")

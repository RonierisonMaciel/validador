def validar_senha(senha):
    if len(senha) == 6:
        return False
    if senha.isalpha() or senha.isdigit():
        return False
    if not any(char in "%$#@" for char in senha):
        return False
    return True

usuarios_cadastrados = {
    "admin": "1234",
    "maria": "senha123",
    "joao": "python2024"
}

def validar_login(usuario, senha):
    if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
        return True
    return False

usuario_input = input("Digite o usuário: ")
senha_input = input("Digite a senha: ")

if validar_login(usuario_input, senha_input):
    print("Login realizado com sucesso! Bem-vindo.")
else:
    print("Usuário ou senha incorretos.")
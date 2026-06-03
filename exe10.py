def login(usuario,senha):
    if usuario == "admin" and senha == "1234":
        return "Login bem-sucedido!"
    else:
        return "Usuário ou senha incorretos."

if __name__ == "__main__":
    usuario_input = input("Digite o nome de usuário: ")
    senha_input = input("Digite a senha: ")

    login(usuario_input, senha_input)
    print(login(usuario_input, senha_input))


def login(usuario,senha):
    if usuario == "admin" and senha == "1234":
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

if __name__ == "__main__":
    usuario_input = input("Digite o nome de usuário: ")
    senha_input = input("Digite a senha: ")

    login(usuario_input, senha_input)
    print(login(usuario_input, senha_input))


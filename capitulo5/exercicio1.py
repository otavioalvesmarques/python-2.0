def validarlogin(nome, senha):
    if (nome == "jose" and senha == "senha1234"):
        return print("seja bem vindo", nome, senha)
    else:
        return print("senha ou login invaldos")


print("=== insira o su nome ===")
nome = input()
print("===digite uma senha === ")
senha = input()


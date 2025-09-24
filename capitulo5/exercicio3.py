def operacoes_basicas(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Erro: Divisão por zero"
    return soma, subtracao, multiplicacao, divisao

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma, subtracao, multiplicacao, divisao = operacoes_basicas(num1, num2)
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
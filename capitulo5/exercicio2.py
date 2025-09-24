def soma_e_subtrair(val1,val2,val3,val4):
    soma = val1 + val2 + val3 + val4
    return soma - 10


num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
num4 = int(input("Digite o quarto valor: "))

resultado = soma_e_subtrair(num1, num2, num3, num4)
print(f"O resultado da soma e subtração é: {resultado}")
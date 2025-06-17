def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1,numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1,numero2):
    return numero1 // numero2

numero1 = int(input("digite um numero inteiro"))
numero2 = int(input("digite um numero inteiro"))

ResultadoSoma= soma(numero1, numero2)
resultadosubtracao = subtracao(numero1, numero2)
resultadomultiplicacao = multiplicacao(numero1, numero2)
resultadodivisao = divisao(numero1, numero2)


print(" o resultado da função soma", ResultadoSoma )
print(" resultado da função da divisão: ", resultadodivisao)
print(" resultado da função multiplicação: ", resultadomultiplicacao)
print(" resultado da função de subtração", resultadosubtracao)
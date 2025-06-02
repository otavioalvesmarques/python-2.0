numero = int(input("Digite um número de 5 dígitos: "))

d1 = numero // 10000
d2 = (numero // 1000) %10
d3 = (numero // 100) %10
d4 = (numero // 10) %10
d5 = numero % 10

print(f"{d1}")
print(f"{d2}")
print(f"{d3}")
print(f"{d4}")
print(f"{d5}")

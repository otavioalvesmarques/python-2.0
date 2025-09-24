contador = 1 
def tabuada(numero):
    global contador
    if contador > 10:
        return
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
    tabuada(numero)

num = int(input("Digite um número para ver a tabuada: "))
tabuada(num)

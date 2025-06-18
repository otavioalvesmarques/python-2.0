def calculaDiametro(raio):
    return 2 * raio


def calculaCircunferencia(PI, raio):
    return 2 * PI * raio


def calculaArea(PI, raio):
    return PI * (raio ** 2)


raio = float(input("insira um numero do raio"))

PI = 3.14159

diametro = calculaDiametro(raio)
circunferencia = calculaCircunferencia(PI, raio)
area = calculaArea(PI, raio)

print("area: ", area)
print("diameto: ", diametro)
print("circunferencia: ", circunferencia)

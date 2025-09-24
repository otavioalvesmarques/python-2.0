def centigrados_para_fahrenheit(varC):
    return (9 * varC + 160) / 5


graus_centigrados = float(input("Digite a temperatura em graus Centígrados: "))
fahrenheit = centigrados_para_fahrenheit(graus_centigrados)
print(f"A temperatura em Fahrenheit é: {fahrenheit}")
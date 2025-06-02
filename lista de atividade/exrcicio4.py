populacao = 8009000000
taxa = float(2.7) / 100
for ano in range(1,6):
    populacao += int(populacao * taxa)
    print(f"Ano {ano}: {populacao}")

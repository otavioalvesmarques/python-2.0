precodecapa = 24.95
desconto = precodecapa - (precodecapa * 0.40)
custodofreteprimeiro = desconto + 3.00
custodefreterestante = desconto + 0.75
custototal = custodofreteprimeiro + (custodefreterestante * 59)

print("o preco total de atacado para 60 exemplar é de : ", custototal)
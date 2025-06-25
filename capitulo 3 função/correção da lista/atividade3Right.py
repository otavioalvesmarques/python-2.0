def right_justify(palavra, tamanhoPalavra):
    espaco = " " * (70 - tamanhoPalavra)
    return espaco + palavra

palavra = str(input("digite uma palavra"))
tamanhoPalavra = len(palavra)
jusyificado = right_justify(palavra, tamanhoPalavra)

print(jusyificado)
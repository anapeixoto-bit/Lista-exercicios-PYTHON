def contar_vogais(texto):
    vogais = "aeiou"
    contador = 0

    for letra in texto.lower():
        if letra in vogais:
            contador += 1

    return contador


palavra = input("Digite uma frase: ")
print("Quantidade de vogais:", contar_vogais(palavra))

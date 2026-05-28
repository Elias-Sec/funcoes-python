def contador_de_vogais(texto):
    contador = 0
    for char in texto:
        if char in "aeiou".lower():
            contador += 1
    return contador

texto = input("Digite sua palavra: ")
contador_de_vogais(texto)
print (contador_de_vogais(texto))
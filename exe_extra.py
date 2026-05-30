def palindromo(texto):
    texto_limpo = texto.replace(" ", "").lower()
    
    return texto_limpo == texto_limpo[::-1]

texto_input = input("Digite um texto para verificar se é um palíndromo: ")
if palindromo(texto_input):
    print("O texto é um palíndromo!")
else:
    print("O texto não é um palíndromo.")


def media_lista(numeros):
    if len(numeros) == 0:
        return 0
    else:
        return sum(numeros) / len(numeros)

if __name__ == "__main__":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    numeros = [num1, num2, num3]
    media = media_lista(numeros)
    print("A média dos números é:", media)

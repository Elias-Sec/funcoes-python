def fatorial(n):
    resultado = 1
    for i in range (1,n+1):
        resultado = resultado * i
    return resultado

if __name__ == "__main__":
    num = int(input("Digite seu Número: "))
    print(fatorial(num))

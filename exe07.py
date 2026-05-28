def fatorial(n):
    resultado = 1
    for i in range (1,n+1):
        resultado = resultado * i
    return resultado

num = int(input("Digite seu Número: "))
print(fatorial(num))

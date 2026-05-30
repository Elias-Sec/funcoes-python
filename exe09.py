def contador_regressivo(n):
    
    if n < 0:
        return
    print(n)
    contador_regressivo(n - 1)

num = int(input("Digite um número para o contador regressivo: "))
contador_regressivo(num)

def contador_regressivo(n):
    
    if n < 0:
        return
    print(n)
    contador_regressivo(n - 1)

if __name__ == "__main__":
    num = int(input("Digite um número para o contador regressivo: "))
    contador_regressivo(num)

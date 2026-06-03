def par_ou_impar (numero):
    if numero %2 == 0:
        print ("Par")
    else:
        print ("Impar")

if __name__ == "__main__":
    par_ou_impar (12)
    par_ou_impar (27)

    numero = int(input("Digite um Número: "))
    par_ou_impar (numero)

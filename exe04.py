def maior_numero(a, b):
    if a > b:
        print (f" {a} é o maior Número!")

    elif b > a:
        print (f"{b} é o maior Número!")

    else:
        print ("Os Números são iguais!")



num1 = int(input("Digite seu número: "))
num2 = int(input("Digite seu número: "))
maior_numero(num1,num2)
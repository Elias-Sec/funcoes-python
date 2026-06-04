import exe01 as o
import exe02 as s
import exe03 as poi
import exe04 as mn
import exe05 as cl
import exe06 as cv
import exe07 as f
import exe08 as ml
import exe09 as cr
import exe10 as lg
import exe_extra as pld


while True:
    play = input("Digite o exe desejado ou sair para encerrar o sistema: ").lower()

    if play == "sair":
        print("Obrigado Por Utilizar Nosso Sistema!" )
        break

    if play == "saudacao":
        nome = input("Diga seu Nome: ")
        o.saudacao (nome)
        

    if play == "somar":
        a = int(input("Digite o Primeiro Valor: "))
        b = int(input("Digite o Segundo Valor: "))
        s.somar(a,b)
        print(s.somar(a,b))

    if play == "parouimpar":
        numero = int(input("Digite um Número: "))
        poi.par_ou_impar (numero)
    
    if play == "maiornumero":
        a = int(input("Digite seu número: "))
        b = int(input("Digite seu número: "))
        mn.maior_numero(a,b)

    if play == "calculadora":
        operacao = input("Digite a Operação Deseja: ")
        a = int(input("Digite o Primeiro Número: "))
        b = int(input("Digite o Segundo Número: "))
        cl.calculadora(a, b, operacao)

    if play == "vogais":
        texto = input("Digite sua palavra: ")
        cv.contador_de_vogais(texto)
    
    if play == "fatorial":
        n = int(input("Digite seu Número: "))
        f.fatorial(n)
        print(f.fatorial(n))

    if play == "media":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        num3 = int(input("Digite o terceiro número: "))

        numeros = [num1, num2, num3]
        ml.media_lista(numeros)
        print(ml.media_lista(numeros))

    if play == "contador":
        n = int(input("Digite um número para o contador regressivo: "))
        cr.contador_regressivo(n)

    if play == "login":
        usuario_input = input("Digite o nome de usuário: ")
        senha_input = input("Digite a senha: ")
        lg.login(usuario_input,senha_input)

    if play == "palindromo":
        texto_input = input("Digite um texto para verificar se é um palíndromo: ")
        if pld.palindromo(texto_input):
            print("O texto é um palíndromo!")
        else:
            print("O texto não é um palíndromo.")
        pld.palindromo(texto_input)
def calculadora(a, b, operacao):
  resultado = 0
  if operacao == "+":
    resultado = a + b
  elif operacao == "-":
    resultado = a - b
  elif operacao == "*":
    resultado = a * b
  else:
    resultado = a / b
  print(resultado)  

if __name__ == "__main__":
  operacao = input("Digite a Operação Deseja: ")
  a = int(input("Digite o Primeiro Número: "))
  b = int(input("Digite o Segundo Número: "))

  calculadora(a,b,operacao)
  print (calculadora(a,b,operacao))
    
def calculadora(a, b, operacao):
  if operacao == "+":
    result = a + b
  elif operacao == "-":
    result = a - b
  elif operacao == "*":
    result = a * b
  else:
    result = a / b
  return result    


operacao = input("Digite a Operação Deseja: ")
a = int(input("Digite o Primeiro Número: "))
b = int(input("Digite o Segundo Número: "))

calculadora(a,b,operacao)
print (calculadora(a,b,operacao))
    
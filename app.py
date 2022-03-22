def soma(n1, n2):
  return float(num1) + float(num2)
def divisao(n1, n2):
  return float(num1) / float(num2)
def multiplicacao(n1, n2):
  return float(num1) * float(num2)
op = input("Qual a operação? ")
num1 = input("Insira o primeiro numero: ")
num2 = input("Insira o segundo numero: ")
if(op == "soma"):
  print(soma(num1, num2))
if(op == "divisao"):
  print(divisao(num1, num2))
if(op == "multiplicacao"):
  print(multiplicacao(num1, num2))
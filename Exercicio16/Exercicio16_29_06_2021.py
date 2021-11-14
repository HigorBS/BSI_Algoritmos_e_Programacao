"""
Um trabalhador recebeu o seu salário e o depositou em sua conta corrente bancária.
Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. Sabe-se que cada operação bancária de retirada 
paga um imposto de 0.38% sobre o valor retirado e o saldo inicial da conta está zerado.
Desenvolva um algoritmo que receba o salário do trabalhador, o valor do primeiro cheque, o valor do segundo cheque e
mostre ao final quanto sobrou na conta do trabalhador.
"""
#variáveis
salario = 0.0
cheque1 = 0.0
cheque2 = 0.0
imposto = 0.0
saldo = 0.0

#execução
salario = float(input("Informe o salário do trabalhador: "))
cheque1 = float(input("Digite o valor do primeiro cheque: "))
cheque2 = float(input("Digite o valor do segundo cheque: "))

imposto = (cheque1 * 0.0038) + (cheque2 * 0.0038)
saldo = salario - cheque1 - cheque2 - imposto

print("O saldo final da conta do trabalhador é de R$", str(saldo))
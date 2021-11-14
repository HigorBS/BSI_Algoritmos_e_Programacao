"""
Faça um algoritmo que solicite N números inteiros.
Ao final o algoritmo deve informar o maior número digitado.
OBS: Fazer utilizando o comando FOR.
"""

contador = 0
numero = 0
maior = 0

contador = int(input("Digite a quantidade de números para a comparação: "))

for contador in range(0,contador,1):
    numero = int(input("Digite um número inteiro: "))
    if(numero > maior):
        maior = numero

print("Maior número digitado: ", maior)
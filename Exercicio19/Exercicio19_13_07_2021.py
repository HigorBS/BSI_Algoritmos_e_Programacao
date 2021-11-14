numero = 1
maior = 0
menor = 9999999

while numero != 0:
    numero = int(input("Informe um número inteiro (o número 0 finaliza o programa):"))
    if(numero != 0):
        if(numero < menor):
            menor = numero
        if(numero > maior):
            maior = numero

if(maior != 0 and menor != 9999999):
    print("Maior número digitado: ", str(maior))
    print("Menor número digitado: ", str(menor))
else:
    print("Nenhum número válido informado.")

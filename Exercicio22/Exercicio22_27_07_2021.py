#variáveis
numero1 = 0.0
numero2 = 0.0
numero3 = 0.0
resultado = 0.0
media = ""

#função
def calcularMedia(n1, n2, n3, med):
    if(med == "A"):
        resultado = (n1 + n2 + n3) / 3
    else:
        resultado = (n1 * 5 + n2 * 3 + n3 * 2) / 10
    return resultado

#algoritmo
numero1 = float(input("Digite a primeira nota: "))
numero2 = float(input("Digite a segunda nota: "))
numero3 = float(input("Digite a terceira nota: "))
media = input("Escolha o tipo de média: A - aritmética // P - ponderada. ")

while(media != "A" and media != "P"):
    print("Opção incorreta.")
    media = input("Escolha o tipo de média: A - aritmética // P - ponderada. ")

resultado = calcularMedia(numero1, numero2, numero3, media)

if(media == "A"):
    media = "Aritmética"
else:
    media = "Ponderada"


print("Média: ", media, ", resultado: ", resultado)
"""
Construa um algoritmo que, recebendo os valores de vendas do mês de determinado vendedor (VM) e o nome do mesmo (NOME). 
Ao final apresente o nome e a mensagem de acordo com a regra:
- Caso venda superior a R$ 50.000,00 mostre a mensagem "A venda está ótima";
- Caso a venda seja menor do que R$ 10.000,00 mensagem: "A venda está baixa";
- Quando o valor da venda estiver entre R$ 10.000,00 (inclusive) e R$ 50.000,00 (inclusive) mensagem: “A venda está ideal”.
"""

nome = ""
vendas = 0.0

nome = input("Digite o nome do vendedor: ")
vendas = float(input("Informe o valor das vendas do mês do vendedor: "))

if(vendas > 50000):
    mensagem = "A venda está ótima."
else:
    if(vendas >= 10000 and vendas <= 50000):
        mensagem = "A venda está ideal."
    else:
        mensagem = "A venda está baixa."

print("Funcionário: ", nome, ". ", mensagem)
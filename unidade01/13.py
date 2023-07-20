# 13. Elabore um programa que efetue a 
# apresentação do valor da conversão em dólar 
# de um valor lido em real. O programa deve 
# solicitar a cotação do dólar e também a 
# quantidade de reais disponível com o usuário, 
# para que seja apresentado o valor em moeda americana.


cotacao_dolar = float(input("Digite a cotação do dólar: "))
quantidade_reais = float(input("Digite a quantidade de reais: "))

valor_dolares = quantidade_reais / cotacao_dolar

print(f"Valor em dólares: {valor_dolares}")

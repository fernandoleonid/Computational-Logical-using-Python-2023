# 12. Elabore um programa que efetue a apresentação do 
# valor da conversão em real de um valor lido em dólar. 
# O programa deve solicitar o valor da cotação do dólar 
# e também a quantidade de dólares disponível com o 
# usuário, para que seja apresentado o valor em moeda 
# brasileira.

cotacao_dolar = float(input("Digite a cotação do dólar: "))
quantidade_dolares = float(input("Digite a quantidade de dólares: "))

valor_reais = cotacao_dolar * quantidade_dolares

print(f"Valor em reais: {valor_reais}")
# 11. Calcule e apresente o valor de uma prestação 
# em atraso, utilizando a fórmula 
# PRESTACAO = VALOR + (VALOR * TAXA/100) * TEMPO.

VALOR = float(input("Digite o valor da prestação: "))
TAXA = float(input("Digite a taxa de juros: "))
TEMPO = int(input("Digite o tempo de atraso (em meses): "))

PRESTACAO = VALOR + (VALOR * TAXA/100) * TEMPO

print(f"Valor da prestação em atraso: ${PRESTACAO}")

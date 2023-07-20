# 15. Elabore um programa de computador que efetue a 
# leitura de quatro valores inteiros (variáveis A, B, C e D).
# Ao final, o programa deve apresentar o resultado do produto
# (variável P) do primeiro com o terceiro valor, e o resultado
# do produto (variável P) do primeiro com o terceiro valor, 
# e o resultado da soma (variável S) do segundo com 
# o quarto valor.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

P = A * C
S = B + D

print(f"Produto (A * C): {P}")
print(f"Soma (B + D): {S}")
# Elabore um programa que leia quatro valores inteiros 
# (variáveis A, B, C e D). Ao final, o programa deve 
# apresentar o resultado do produto (variável P) do 
# primeiro com o terceiro valor, e o resultado da 
# soma (variável S) do egsundo com o quarto valor.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
d = int(input("Digite o valor de D: "))

p = a * c
s = b + d

print (f"Produto de A e C é: {p}")
print (f"A som de B e D é: {s}")
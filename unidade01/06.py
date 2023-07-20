# Elabore um programa que efetue a leitura de três valores
# (A, B e C) e apresente como resultado final o quadrado 
# da soma dos três valores lidos.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

soma_quadrados = a ** 2 + b ** 2 + c ** 2

print(f"A soma dos quadrados de A, B e C é: {soma_quadrados}")
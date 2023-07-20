# 10. Calcule e apresente o valor do volume de uma lata de óleo, 
# utilizando a fórmula: volume = π * raio ** 2 * altura. 
# Considere o valor de π como 3.1415.

import math

raio = float(input("Digite o valor do raio da lata de óleo: "))
altura = float(input("Digite o valor da altura da lata de óleo: "))

volume = math.pi * raio ** 2 * altura

print(f"O volume da lata de óleo é: {volume}")

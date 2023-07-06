# Leia dois valores (inteiros, reais ou caracteres) 
# para as variáveis A e B, e efetue a troca dos valores 
# de forma que a variável A passe a possuir o valor da 
# variável B e a variável B passe a possuir o valor da 
# variável A. Apresente os valores trocados.

a = input("Digite o valor da A: ")
b = input("Digite o valor de B: ")

aux = a
a = b
b = aux

print ("Valores trocados:")
print (f"A = {a}")
print (f"B = {b}")
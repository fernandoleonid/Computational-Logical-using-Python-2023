# Crie um programa que solicite ao usuário 
# uma lista de números inteiros e retorne 
# a soma de todos os elementos da lista.

lista_numeros = []

resposta = 's'

while resposta == 's':
    numero = input("Digite um número: ")
    lista_numeros.append(numero)
    resposta = input ("Deseja continuar [s/n]: ")

print (lista_numeros)

numero = int(input("Digite um número: "))
fatorial = 1

for contador in range(1, numero + 1):
    fatorial *= contador

print(f"O fatorial de {numero} é {fatorial}.")


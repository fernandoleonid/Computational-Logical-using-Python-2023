# 8. Crie um programa que solicite ao usuário o 
# início, o fim e o número para a tabuada. 
# Em seguida, exiba a tabuada desse número no 
# intervalo determinado.

numero = int(input("Digite um número: "))
inicio = int(input("Digite o ínicio da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))
                
for contador in range(inicio, fim+1):
    resultado = numero * contador
    print (f"{numero} X {contador} = {resultado}")

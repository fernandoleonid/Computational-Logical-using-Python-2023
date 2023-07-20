# 8. Leia dois inteiros (variáveis A e B) e 
# imprima o resultado do quadrado da diferença 
# do primeiro valor pelo segundo.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

diferenca = A - B
resultado = diferenca ** 2

print(f"O quadrado da diferença entre A e B é: {resultado}")
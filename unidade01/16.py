# 16. Em uma eleição sindical concorreram ao cargo de 
# presidente três candidatos (A, B e C). Durante a 
# apuração dos votos foram computados votos nulos e 
# votos em branco, além dos votos válidos para cada 
# candidato. Deve ser criado um programa de computador 
# que efetue a leitura da quantidade de votos válidos 
# para cada candidato, além de efetuar também a leitura 
# da quantidade de votos nulos e votos em branco. 
# Ao final o programa deve apresentar o número total 
# de eleitores, considerando votos válidos, nulos e 
# em branco; o percentual correspondente de votos 
# válidos em relação à quantidade de eleitores; 
# o percentual correspondente de votos válidos do 
# candidato A em relação à quantidade de eleitores; 
# o percentual correspondente de votos válidos do 
# candidato B em relação à quantidade de eleitores; 
# o percentual correspondente de votos válidos do 
# candidato C em relação à quantidade de eleitores; 
# o percentual correspondente de votos nulos em relação 
# à quantidade de eleitores; e por último o percentual 
# correspondente de votos em branco em relação à 
# quantidade de eleitores.

votos_validos_A = int(input("Digite a quantidade de votos válidos do candidato A: "))
votos_validos_B = int(input("Digite a quantidade de votos válidos do candidato B: "))
votos_validos_C = int(input("Digite a quantidade de votos válidos do candidato C: "))
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_branco = int(input("Digite a quantidade de votos em branco: "))

total_eleitores = votos_validos_A + votos_validos_B + votos_validos_C + votos_nulos + votos_branco

percentual_validos = (votos_validos_A + votos_validos_B + votos_validos_C) / total_eleitores * 100
percentual_validos_A = votos_validos_A / total_eleitores * 100
percentual_validos_B = votos_validos_B / total_eleitores * 100
percentual_validos_C = votos_validos_C / total_eleitores * 100
percentual_nulos = votos_nulos / total_eleitores * 100
percentual_branco = votos_branco / total_eleitores * 100

print(f"Número total de eleitores: {total_eleitores}")
print(f"Percentual de votos válidos: {percentual_validos}%")
print(f"Percentual de votos válidos do candidato A: {percentual_validos_A:.2f}%")
print(f"Percentual de votos válidos do candidato B: {percentual_validos_B:.2f}%")
print(f"Percentual de votos válidos do candidato C: {percentual_validos_C:.2f}%")
print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos em branco: {percentual_branco:.2f}%")
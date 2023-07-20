# 9. Leia o valor correspondente ao salário mensal 
# (variável SM) de um trabalhador e também o valor 
# do percentual de reajuste (variável PR) a ser 
# atribuído. Apresente o valor do novo salário (variável NS).

SM = float(input("Digite o valor do salário mensal: "))
PR = float(input("Digite o percentual de reajuste: "))

NS = SM + (SM * PR / 100)

print(f"Novo salário: {NS}")
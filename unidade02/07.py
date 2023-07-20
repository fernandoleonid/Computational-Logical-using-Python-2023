# 7. Crie um programa que solicite a média 
# e a frequência de um aluno, e determine 
# sua situação. Se a média for maior ou 
# igual a 5 e a frequência for maior ou 
# igual a 75%, o aluno está aprovado. 
# Se a média for menor que 5 e a frequência 
# for menor que 75%, o aluno está reprovado. 
# Em qualquer outro caso, o aluno está de 
# recuperação.

media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite a frequência do aluno: "))

if media >= 5 and frequencia >= 75:
    print ("Aluno aprovado")
elif media < 5 and frequencia < 75:
    print ("Aluno Reprovado")
else:
    print ("Aluno em recuperação")

"""
Crie um programa que 
1 - 
    1.1 leia duas notas de um aluno 
2 - calcule a sua média, 
3 - mostrando uma mensagem no final, 
de acordo com a média atingida:
4 - 
    4.1 - Média até 4.9: REPROVADO
    4.2 - Média entre 5.0 e 6.9: RECUPERAÇÃO
    4.3 - Média 7.0 ou superior: APROVADO
"""

nota1 = float(input("qual a primeira nota? \n"))
nota2 = float(input("qual a segunda nota? \n"))
print("-------------------")

calc = ( nota1 + nota2 ) / 2

print("calculo de media")
print("Média 7.0 ou superior: APROVADO")
print("Média entre 5.0 e 6.9: RECUPERAÇÃO")
print("Média até 4.9: REPROVADO")

print("-------------------")

if calc >= 7:
    print("Média",calc)
    print("Aluno APROVADO")
elif calc >= 5:
    print("Média",calc)
    print("Aluno em RECUPERAÇÃO")
else:
    print("Média",calc)
    print("Aluno REPROVADO")



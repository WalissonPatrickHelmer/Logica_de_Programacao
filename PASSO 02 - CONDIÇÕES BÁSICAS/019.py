"""
Crie um algoritmo que 
1 - leia o nome  
2 - 
    2.1 - as duas notas de um aluno,
3- calcule a sua média 
4 - e mostre na tela. No final,
5 -  analise a média e mostre se o aluno teve ou
não um bom aproveitamento (se ficou acima da média 7.0).

"""
nome = str(input("Qual o seu nome ? \n"))
nota1 = float(input("Qual o valor da primeira nota? \n"))
nota2 = float(input("Qual o valor da segunda nota? \n"))

calc = (nota1 + nota2) / 2

if calc > 7:
    print(F"{nome} ficou com media {calc}, muito bom o seu aproveitamento") 
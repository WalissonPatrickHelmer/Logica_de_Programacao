"""
Faça um algoritmo que leia um determinado ano e mostre se ele é ou não
BISSEXTO.

"""

ano = int(input(" Digite o ano do seu nascimento \n"))

if ano % 4 == 0:
    print(" O ano do seu nascimento e bissexto")
else:
    print("O ano do seu nascimento não e bissexto")
"""
Desenvolva um programa que 
1 - leia um número inteiro e 
2 - mostre se ele é PAR ou ÍMPAR.

"""

numero = int(input("Digite um valor"))

div = numero % 2

if div == 1:
    print("IMPAR")
else:
    print("PAR")
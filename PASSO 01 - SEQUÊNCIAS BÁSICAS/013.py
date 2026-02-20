"""
013
Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
seu novo salário, com 15% de aumento.
"""

salario = float(input("qual o salario ? \nR$"))

salario_novo = salario * 1.15

print(f"Salario novo e R${salario_novo:.2f}")
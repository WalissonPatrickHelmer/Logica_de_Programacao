"""
12
Crie um programa que leia o preço de um produto, 
calcule e mostre o seu
PREÇO PROMOCIONAL, com 5% de desconto.
"""

valor = float(input("Qual o valor do produto? \nR$"))

valor_com_desconto = valor  * 0.95

print(f"O valor final do produto com desconto e: R${valor_com_desconto:.2f} ")
"""
009
Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
"""

valor = float(input("Qual valor vc tem hoje ? "))

dolar = valor / 3.45

print(f"Vc tem R${valor:.2f} e convertido, vai ter U${dolar:.2f}")
"""
11
Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
segundo grau e mostre o valor de Delta.
"""


a = float(input("Digite o valor de A: \n"))
b = float(input("Digite o valor de B: \n"))
c = float(input("Digite o valor de C: \n"))


delta = b**2 - 4 * a * c

print(f"O valor de delta e: {delta}")


"""
10
Faça um algoritmo que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
"""
altura = float(input("Qual a altura da parede ? \n"))
comprimento = float(input("Qual o comprimento da parede ? \n"))

metros_quadrado = comprimento * altura

tinta = metros_quadrado / 2

print(f"A quantidade de litros de tinta a ser comprada e {tinta} litros ")

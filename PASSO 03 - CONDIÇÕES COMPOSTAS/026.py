"""
026 
Escreva um algoritmo que
1 - 
    1.1 leia dois números inteiros 
2 - compare-os, 
3 - mostrando na tela uma das mensagens abaixo:
    3.1 - O primeiro valor é o maior
    3.2 - O segundo valor é o maior
    3.3 - Não existe valor maior, os dois são iguais
"""

numero1 = int(input("Digite um numero: \n"))
numero2 = int(input("Digite outro numero: \n"))

if numero1 > numero2:
    print("O valor 1 e maior que o valor 2")

elif numero1 < numero2:
    print("O valor 1 e menor que o valor 2")

else:
    print("O valor 1 e igual que o valor 2")
"""
006 
Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
sucessor.
Ex:
Digite um número: 9
O antecessor de 9 é 8
O sucessor de 9 é 10

"""
numero = int(input("Digite um numero \n"))

antecessor = numero - 1
sucessor = numero + 1

print(f"O antecessor e {antecessor}, o numero digitado e {numero}, e o sucessor e {sucessor}.")


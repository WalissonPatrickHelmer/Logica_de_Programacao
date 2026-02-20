"""
Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
para todos, mas especialmente para mulheres. Faça um programa que 
1 - leia nome
2 - sexo 
3 - valor das compras do cliente e 
4 - calcule o preço com desconto. Sabendo que:
    4.1 - Homens ganham 5% de desconto
    4.2 - Mulheres ganham 13% de desconto
"""
nome = str(input("Qual e o seu nome ? \n"))
sexo = int(input("digite \n1 masculino \n0 femino \n "))
valor = float(input("Qual o valor do produto? \nR$ "))
desconto = 0

if sexo == 1:
    desconto = 5
    valor_final = valor / 100 * 95
    print(f"Sr {nome}, o valor do produto e R${valor:.2f} e seu desconto e de 5%,\n O valor final que vai pagar hoje e R${valor_final:.2f} ")
else:
    desconto = 15
    valor_final = valor / 100 * 85
    print(f"Sra {nome}, o valor do produto e R${valor:.2f} e seu desconto e de 15%,\n O valor final que vai pagar hoje e R${valor_final:.2f} ")




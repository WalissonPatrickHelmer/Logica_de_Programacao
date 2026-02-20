"""
014
A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado
"""

km = float(input("Quanto km rodou com o veiculo? \n km:"))
dia = int(input("quantos dias ficou com o veiculo? \n dias:"))

preco = ((km * 0.2) + ( dia * 90 ))
print(f"O valor a pagar direto e \n R${preco:.2f} \n")

km_total = km * 0.2
dia_total = dia * 90
print("------------------")
preco_total = km_total + dia_total

print(f"O valor a pagar separado e \nkm rodado: R${km_total:.2f}. \ndias com o veiculo: R${dia_total:.2f}. \nSomados R${preco_total:.2f}.")
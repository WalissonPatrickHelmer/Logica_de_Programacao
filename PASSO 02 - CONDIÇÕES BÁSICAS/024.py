"""
Faça um algoritmo que pergunte 
1 - a distância que um passageiro deseja percorrer em Km.
2 - Calcule o preço da passagem, 
3 - cobrando R$0.50 por Km para viagens até 200Km 
    3.1 R$0.45 para viagens mais longas.
"""
distancia = float(input("Qual e a distancia da viagem? \n"))
calc = 0

if distancia <= 200:
    calc = 0.45
    print(f"o valor por km e {calc:.2f}")
else:
    calc = 0.50
    print(f"o valor por km e {calc:.2f}")

valor = calc * distancia
print(f"O valor da passagem e R${valor:.2f}")


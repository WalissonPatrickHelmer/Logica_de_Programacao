"""
Escreva um programa que 
1 - leia o ano de nascimento de um rapaz 
2 - e mostre a sua situação em relação ao alistamento militar.

3 - Se estiver antes dos 18 anos,
 mostre quantos anos faltam para o alistamento.
3.1 - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.
"""
ano = int(input("Qual o ano do seu nascimento?\n"))

ano_2026 = 2026 - ano
print(f"sua idade e {ano_2026} anos")
if ano_2026 >= 18:
    print("Ja pode se alistar")
else:    
    ano_2026 = 18 - ano_2026
    print(f"falta para o seu alistamento aproximadamente {ano_2026} anos")

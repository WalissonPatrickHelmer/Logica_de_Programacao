"""
16) [DESAFIO] 
Escreva um programa para calcular a redução do tempo de vida de um fumante. 

1 - Pergunte a quantidade de cigarros fumados por dias
2 - quantos anos ele já fumou. 
3 - Considere que um fumante perde 10 min de vida a cada cigarro. 
4 - Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
"""

cigarros = int(input("Quanto cigarros vc fuma por dia ?\n"))
anos = int(input("A quantos anos vc fuma? \n"))

total_de_cigarros = cigarros * ( anos * 365 )
print(f"na vida vc ja fumou {total_de_cigarros} cigarros")

minutos_perdidos = total_de_cigarros * 10
dias_perdidos = minutos_perdidos / ( 60 * 24 )

print(f"Vc perdeu aproximadamente {dias_perdidos:.2f} dias de vida.")

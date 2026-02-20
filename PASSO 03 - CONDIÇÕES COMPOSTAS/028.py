"""
Faça um programa que 
1 - 
    1.2 leia a largura e o comprimento de um terreno
    retangular,
2 - calculando e 
3 - mostrando a sua área em m². 
4 - O programa também devemostrar a classificação 
    desse terreno,de acordo com a lista abaixo:

    4.2 - Abaixo de 100m² = TERRENO POPULAR
    4.3 - Entre 100m² e 500m² = TERRENO MASTER
    4.4 - Acima de 500m² = TERRENO VIP
"""

larg = float(input("Qual a largura do terreno: \n"))
comp = float(input("Qual a comprimento do terreno: \n"))

calc = larg * comp
print(f"O terreno tem {calc:.2f}m²")

if calc > 500:
    print("TERRENO VIP")    
elif calc > 300:
    print("TERRENO MASTER")
else:
    print("TERRENO POPULAR")
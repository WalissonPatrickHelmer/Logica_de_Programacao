"""
008
Desenvolva um programa que leia uma distância em metros e mostre os valores
relativos em outras medidas.
Ex:
Digite uma distância em metros: 185.72
A distância de 85.7m corresponde a:
0.18572Km 1.8572Hm 18.572Dam 
1857.2dm 18572.0cm 185720.0mm
"""

distancia = float(input("Qual a distância percorrida em metros? \n"))

km = distancia / 1000
Hm = distancia / 100
Dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

print(f"A distancia percorrda em {distancia} metros")
print(f"{km} km")
print(f"{Hm} Hm")
print(f"{Dam} Dam")
print(f"{dm} dm")
print(f"{cm} cm")
print(f"{mm} mm")
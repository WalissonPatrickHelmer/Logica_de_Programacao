"""
Escreva um programa que pergunte a velocidade de um carro.
1 - Caso ultrapasse 80Km/h, 
2 - exiba uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba
o valor da multa,
cobrando R$5 por cada Km acima da velocidade permitida

"""

velocidade = int(input("Qual a velocidade do veiculo ? \n"))
valor_multa = 0

if velocidade > 79:
    print("multado")
    valor_multa = ( velocidade - 79) * 5
    print(f"O valor da multa e de R${valor_multa}")
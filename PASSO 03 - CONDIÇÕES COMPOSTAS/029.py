"""
Desenvolva um programa que 
1 - leia o nome de um funcionário, 
2 - seu salário,
3 - quantos anos ele trabalha na empresa e
4 -  mostre seu novo salário, reajustado de
        acordo com a tabela a seguir:

    4.2- Até 3 anos de empresa: aumento de 3%
    4.3- entre 3 e 10 anos: aumento de 12.5%
    4.4- 10 anos ou mais: aumento de 20%
"""

nome = str(input("Qual e o seu nome? \n nome:"))
salario = int(input("Qual e o seu salario? \nR$"))
anos = int(input("A quantos anos trabalha na empresa? \n tempo:"))

if anos  >= 10:
    salario_novo = salario * 1.2
    print(f"O seu novo salario {nome} e R${salario_novo:.2f},")

elif anos >= 3:
    salario_novo = salario * 1.125
    print(f"O seu novo salario {nome} e R${salario_novo:.2f},")
else:
    salario_novo = salario * 1.03
    print(f"O seu novo salario {nome} e R${salario_novo:.2f},")

print(f"Nos agradecemos pelos tempo que esta com nos {nome}!")
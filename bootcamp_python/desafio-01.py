"""
descricao: Calculo de bonus com entrada do usuario
autor: wellington moreira
"""

# Desafio 
print('\n'+'-'*100)
print(
"""
Desafio
 
Escreva um programa em Python que solicita ao usuário para:
	- digitar seu nome, 
	- o valor do seu salário mensal e,
	- o valor do bônus que recebeu.

O programa deve:
	- imprimir uma mensagem saudando o usuário pelo nome 
	- informar o valor do salário em comparação com o bônus recebido.
    
Constante:
	- o valor do bônus fixo é de 1000
""")

print('-'*100+'\n')


nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário atual: ').replace(',','.'))
bonus = float(input('Digite seu bonus atual(%): ').replace(',','.'))
bonus_fixo = 1000
kpi = bonus_fixo + (salario*bonus)

print(f'\nOlá {nome}, O cálculo do KPI do bônus é de: {kpi}\n ')

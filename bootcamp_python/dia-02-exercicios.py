"""
descricao: exercicios de fixacao
autor: wellington moreira
"""

def formata_titulo(titulo:str):
    print('\n'+'-'*100)
    print(titulo)
    print('-'*100)

# inteiros: exercício 01-05
class Inteiros:
    def exercicio_01(self):
        formata_titulo('Escreva um programa que soma dois números inteiros inseridos pelo usuário.')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        return f'Soma de {num1} + {num2} = {num1+num2}' 
    def exercicio_02(self):
        formata_titulo('Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5')
        num = int(input('Digite um numero: '))
        return f'Resto da divisão de {num} por 5 = {num%5}'

    def exercicio_03(self):
        formata_titulo('Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        return f'Multiplicação de {num1} * {num2} = {num1*num2}'

    def exercicio_04(self):
        formata_titulo('Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        return f'Divisão inteira de {num1} por {num2} = {num1//num2}'

    def exercicio_05(self):
        formata_titulo('Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.')
        num = int(input('Digite um numero: '))
        return f'Quadrado de {num} = {num**2}'

exercicios_inteiros = Inteiros()

print(exercicios_inteiros.exercicio_01())
print(exercicios_inteiros.exercicio_02())
print(exercicios_inteiros.exercicio_03())
print(exercicios_inteiros.exercicio_04())
print(exercicios_inteiros.exercicio_05())

# reais: exercício 06-10
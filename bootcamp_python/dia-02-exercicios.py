"""

descricao: exercicios de fixacao
autor: wellington moreira

"""

# indice:

#     1 - Inteiros - linha 22
#     2 - Reais - linha 51
#     3 - Strings - linha 81
#     4 - Booleanos -
#     5 - try/except e if-

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

# reais: exercício 06-10
class Reais:
    def exercicio_06(self):
        formata_titulo('Escreva um programa que receba dois números flutuantes e realize sua adição.')
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
        return f'Soma de {num1} + {num2} = {num1+num2}'
    
    def exercicio_07(self):
        formata_titulo('Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.')
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
        return f'Média de {num1} + {num2} = {(num1+num2)/2}'

    def exercicio_08(self):
        formata_titulo('Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).')
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
        return f'Potência de {num1} elevado a {num2} = {num1**num2}'

    def exercicio_09(self):
        formata_titulo('Faça um programa que converta a temperatura de Celsius para Fahrenheit.')
        celsius = float(input('Digite a temperatura: '))
        fahrenheit = (float(celsius) * 9 / 5 + 32)
        return f'{celsius} celsius = {fahrenheit} fahrenheit' 

    def exercicio_10(self):
        formata_titulo('Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.')
        raio = float(input('Digite o raio: '))
        return f'Área de um círculo de raio {raio} = {3.14*raio**2}'

class Strings_exercicios:
    def exercicio_11(self):
        formata_titulo('Escreva um programa que receba uma string do usuário e a converta para maiúsculas.')
        string = input('Digite uma string: ')
        return f'{string} em maiúsculas = {string.upper()}'

    def exercicio_12(self):
        formata_titulo('Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.')
        nome = input('Digite seu nome: ')
        return f'{nome} em minúsculas = {nome.lower()}'

    def exercicio_13(self):
        formata_titulo('Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.')
        frase = input('Digite uma frase: ')
        return f'Frase sem espaços: {frase.strip()}'

    def exercicio_14(self):
        formata_titulo('Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.')
        data = input('Digite uma data no formato dd/mm/aaaa: ')
        data_separada = data.split('/')
        return f'Dia: {data_separada[0]}\nMês: {data_separada[1]}\nAno: {data_separada[2]}'

    def exercicio_15(self):
        formata_titulo('Escreva um programa que concatene duas strings fornecidas pelo usuário.')
        string1 = input('Digite a primeira string: ')
        string2 = input('Digite a segunda string: ')
        return f'{string1} + {string2} = {string1+string2}'

# exercicios_inteiros = Inteiros()
# exercicios_reais = Reais()
# exercicios_strings = Strings_exercicios()

# print(exercicios_inteiros.exercicio_01())
# print(exercicios_inteiros.exercicio_02())
# print(exercicios_inteiros.exercicio_03())
# print(exercicios_inteiros.exercicio_04())
# print(exercicios_inteiros.exercicio_05())
# print(exercicios_reais.exercicio_06())
# print(exercicios_reais.exercicio_07())
# print(exercicios_reais.exercicio_08())
# print(exercicios_reais.exercicio_09())
# print(exercicios_reais.exercicio_10())
# print(exercicios_strings.exercicio_11())
# print(exercicios_strings.exercicio_12())
# print(exercicios_strings.exercicio_13())
# print(exercicios_strings.exercicio_14())
# print(exercicios_strings.exercicio_15())
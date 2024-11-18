"""

descricao: exercicios de fixacao
autor: wellington moreira

indice:
    Exercícios
     1 - Inteiros - linha 22
     2 - Reais - linha 50
     3 - Strings - linha 82
     4 - Booleanos - linha 111
     5 - try/except e if -

"""

def formata_titulo(titulo:str):
    print('\n'+'-'*100)
    print(titulo)
    print('-'*100)

# inteiros: exercício 01-05
def exercicio_01():
    formata_titulo('Escreva um programa que soma dois números inteiros inseridos pelo usuário.')
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    return f'Soma de {num1} + {num2} = {num1+num2}' 
def exercicio_02():
    formata_titulo('Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5')
    num = int(input('Digite um numero: '))
    return f'Resto da divisão de {num} por 5 = {num%5}'

def exercicio_03():
    formata_titulo('Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.')
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    return f'Multiplicação de {num1} * {num2} = {num1*num2}'

def exercicio_04():
    formata_titulo('Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.')
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    return f'Divisão inteira de {num1} por {num2} = {num1//num2}'

def exercicio_05():
    formata_titulo('Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.')
    num = int(input('Digite um numero: '))
    return f'Quadrado de {num} = {num**2}'

# reais: exercício 06-10
def exercicio_06():
    formata_titulo('Escreva um programa que receba dois números flutuantes e realize sua adição.')
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    return f'Soma de {num1} + {num2} = {num1+num2}'

def exercicio_07():
    formata_titulo('Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.')
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    return f'Média de {num1} + {num2} = {(num1+num2)/2}'

def exercicio_08():
    formata_titulo('Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).')
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    return f'Potência de {num1} elevado a {num2} = {num1**num2}'

def exercicio_09():
    formata_titulo('Faça um programa que converta a temperatura de Celsius para Fahrenheit.')
    celsius = float(input('Digite a temperatura: '))
    fahrenheit = (float(celsius) * 9 / 5 + 32)
    return f'{celsius} celsius = {fahrenheit} fahrenheit' 

def exercicio_10():
    formata_titulo('Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.')
    raio = float(input('Digite o raio: '))
    return f'Área de um círculo de raio {raio} = {3.14*raio**2}'

# strings: exercício 11-15
def exercicio_11():
    formata_titulo('Escreva um programa que receba uma string do usuário e a converta para maiúsculas.')
    string = input('Digite uma string: ')
    return f'{string} em maiúsculas = {string.upper()}'

def exercicio_12():
    formata_titulo('Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.')
    nome = input('Digite seu nome: ')
    return f'{nome} em minúsculas = {nome.lower()}'

def exercicio_13():
    formata_titulo('Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.')
    frase = input('Digite uma frase: ')
    return f'Frase sem espaços: {frase.strip()}'

def exercicio_14():
    formata_titulo('Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.')
    data = input('Digite uma data no formato dd/mm/aaaa: ')
    data_separada = data.split('/')
    return f'Dia: {data_separada[0]}\nMês: {data_separada[1]}\nAno: {data_separada[2]}'

def exercicio_15():
    formata_titulo('Escreva um programa que concatene duas strings fornecidas pelo usuário.')
    string1 = input('Digite a primeira string: ')
    string2 = input('Digite a segunda string: ')
    print(f'{string1} + {string2} = {string1+string2}')

# Booleanos: exercício 16-20
def exercicio_16():
    formata_titulo('Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.')
    expressao1 = True if input('Digite a primeira expressão: True ou False: ') == 'True' else False
    expressao2 = True if input('Digite a segunda expressão: True ou False: ') == 'True' else False    
    print(f'{expressao1} AND {expressao2} = {expressao1 and expressao2}')

def exercicio_17():
    formata_titulo('Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.')
    expressao1 = True if input('Digite a primeira expressão: True ou False: ') == 'True' else False
    expressao2 = True if input('Digite a segunda expressão: True ou False: ') == 'True' else False    
    print(f'{expressao1} OR {expressao2} = {expressao1 or expressao2}')

def exercicio_18():
    formata_titulo('Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.')
    expressao = True if input('Digite a primeira expressão: True ou False: ') == 'True' else False
    print(f'{expressao} invertido = {not expressao}')

def exercicio_19():
    formata_titulo('Faça um programa que compare se dois números fornecidos pelo usuário são iguais.')
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    print(f'{num1} = {num2} ? : {num1==num2}')

def exercicio_20():
    formata_titulo('Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.')
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    print(f'{num1} != {num2} ? : {num1!=num2}')

exercicio_20()

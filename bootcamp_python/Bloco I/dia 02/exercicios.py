"""

descricao: exercicios de fixacao
    - dia 02 bootcamp python: Inteiros, Reais, Strings e Booleanos
    
indice:
    Exercícios
     1 - Inteiros - linha 22
     2 - Reais - linha 50
     3 - Strings - linha 82
     4 - Booleanos - linha 111
     5 - try/except e if - linha 138

"""

def formata_titulo(titulo:str):
    print('\n'+'-'*100)
    print(titulo)
    print('-'*100)

# inteiros: exercício 01-05
def exercicio_1():
    formata_titulo('Escreva um programa que soma dois números inteiros inseridos pelo usuário.')
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    return f'Soma de {num1} + {num2} = {num1+num2}' 
def exercicio_2():
    formata_titulo('Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5')
    num = int(input('Digite um numero: '))
    return f'Resto da divisão de {num} por 5 = {num%5}'

def exercicio_3():
    formata_titulo('Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.')
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    return f'Multiplicação de {num1} * {num2} = {num1*num2}'

def exercicio_4():
    formata_titulo('Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.')
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    return f'Divisão inteira de {num1} por {num2} = {num1//num2}'

def exercicio_5():
    formata_titulo('Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.')
    num = int(input('Digite um numero: '))
    return f'Quadrado de {num} = {num**2}'

# reais: exercício 06-10
def exercicio_6():
    formata_titulo('Escreva um programa que receba dois números flutuantes e realize sua adição.')
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    return f'Soma de {num1} + {num2} = {num1+num2}'

def exercicio_7():
    formata_titulo('Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.')
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    return f'Média de {num1} + {num2} = {(num1+num2)/2}'

def exercicio_8():
    formata_titulo('Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).')
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    return f'Potência de {num1} elevado a {num2} = {num1**num2}'

def exercicio_9():
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

# try except e if: 21-25
def exercicio_21():
    formata_titulo('Conversor de Temperatura')
    try:
        choice = int(input('Digite 1 para converter de Celsius para Fahrenheit ou 2 para converter de Fahrenheit para Celsius: '))
        if choice == 1:
            temperatura = float(input('Digite a temperatura em Celsius: ').replace(',', '.'))
            if temperatura is not None or temperatura is not isinstance(float):
                temperatura_convertida = (temperatura*9/5)+32
                print(f'{temperatura} graus Celsius = {temperatura_convertida:.2f} graus Fahrenheit')
        
        elif choice == 2:
            temperatura = float(input('Digite a temperatura em Fahrenheit: ').replace(',', '.'))
            if temperatura is not None or temperatura is not isinstance(float):
                temperatura_convertida = (temperatura-32)*5/9
                print(f'{temperatura} graus Fahrenheit = {temperatura_convertida:.2f} graus Celsius')
        
        else:
            print('Opção inválida')
    
    except ValueError:
        print('Temperatura inválida')

def exercicio_22():
    formata_titulo('Verificador de Palíndromo')

    palavra = input('Digite uma palavra: ').strip().split(' ')
    try:
        palavra = palavra[0]
        print(palavra)
        if palavra is None:
            exit()

        if palavra.isnumeric():
            exit('Palavra inválida, tente sem números')
        
        if not isinstance(palavra, str):
            raise ValueError    
        
        if len(palavra) == 0:
            raise ValueError
        
        palavra_invertida = palavra[::-1]

        if palavra == palavra_invertida:
            print(f'{palavra} é palíndromo')
        else:
            print(f'{palavra} nao é palíndromo')

    except Exception as e:
        print(f'Palavra inválida, erro {e}')

def exercicio_23():
    formata_titulo('Calculadora Simples')

    try:
        num1 = float(input('Digite o primeiro valor: ').strip().replace(',', '.'))
        num2 = float(input('Digite o segundo valor: ').strip().replace(',', '.'))
        operador = input('Digite o operador (+, -, *, /): ')

        if num1 is None or num2 is None or operador is None:
            raise ValueError
        
        if not isinstance(num1, float) or not isinstance(num2, float):
            raise ValueError
 
        if operador not in ['+', '-', '*', '/']:
            raise ValueError
        
        if operador == '+':
            print(f'{num1} + {num2} = {num1+num2}')
        elif operador == '-':
            print(f'{num1} - {num2} = {num1-num2}')
        elif operador == '*':
            print(f'{num1} * {num2} = {num1*num2}')
        elif operador == '/':
            if num2 == 0:
                raise ZeroDivisionError('Divisão por zero')
            print(f'{num1} / {num2} = {num1/num2}')
        else:
            print('Operador inválido')

    except ValueError:
        print('Valores inválidos')

def exercicio_24():
    formata_titulo('Classificador de Números, Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".')

    try:
        num = int(input('Digite um numero: '))

        if num is None:
            raise ValueError('Número inválido')
        
        if not isinstance(num, int):
            raise TypeError('Entrada inválida')

        if num > 0:
            print(f'{num} eh positivo')
        elif num < 0:
            print(f'{num} eh negativo')
        else:
            print(f'{num} eh zero')
        
        if num % 2 == 0:
            print(f'{num} eh par')
        else:
            print(f'{num} eh impar')
    except ValueError:
        print('Tem que ser um numero')

def exercicio_25():
    formata_titulo('Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.')

    try:
        
        numeros = input('Digite uma lista de números separados por vírgula: ').split(',')
        numeros = [int(num) for num in numeros if num.strip().isdigit()]
        print(numeros)
    
    except ValueError:
        print('Tem que ser um numero')

if __name__ == '__main__':

    exercicio_1()
    exercicio_2()
    exercicio_3()
    exercicio_4()
    exercicio_5()
    exercicio_6()
    exercicio_7()
    exercicio_8()
    exercicio_9()
    exercicio_10()
    exercicio_11()
    exercicio_12()
    exercicio_13()
    exercicio_14()
    exercicio_15()
    exercicio_16()
    exercicio_17()
    exercicio_18()
    exercicio_19()
    exercicio_20()
    exercicio_21()
    exercicio_22()
    exercicio_23()
    exercicio_24()
    exercicio_25()
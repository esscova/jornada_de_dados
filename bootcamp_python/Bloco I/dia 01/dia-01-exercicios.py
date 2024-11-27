
# Exercício 01
# Crie programa que o shale digita o seu nome e retorna o número de caracteres
print('\n'+ '-'*100)
print('Exercício 01: Crie programa que o usuário digita o seu nome e retorna o número de caracteres')
print('-'*100)
nome = input('Digite seu nome: ')
qt_caracteres = len(nome)
print(f'O nome: {nome},  possui {qt_caracteres} caracteres')


# Exercício 02
# Criar um programa onde o usuário digite dois valores e apareça a soma
print('\n'+'-'*100)
print('Exercício 02: Criar um programa onde o usuário digite dois valores e apareça a soma')
print('-'*100)
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
soma = valor1+valor2
print(f'Soma de {valor1} +  {valor2} = {soma}\n')

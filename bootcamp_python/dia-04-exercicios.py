"""
descrição: 
    - Resolução dos exercicios, bootcamp Python, dia 04

autor:
    - wellington moreira
    - wsantos08@hotmail.com

versao python: 
    - 3.12.4

"""

# Exercício 01
# Lista de números ao quadrado: Criar uma lista com os números ao quadrado de 1 a 10.
def exercicio_01() -> None:
    numeros:list = [num**2 for num in range(1, 11)]
    print(numeros)

# Exercício 02
# Listas: Modifique a lista a seguir:["Python", "Java", "C++", "JavaScript"],removendo C++ e adicionando Ruby.
def exercicio_02() -> list:
    lista:list = ["Python", "Java", "C++", "JavaScript"]
    lista.remove('C++')
    lista.append('Ruby')
    return lista

# Exercício 03
# Dicionarios: Criar um dicionário de livros que contenha 'titulo', 'autor' e 'ano' ao fim imprima as informações do livro
def exercicio_03(titulo:str, autor:str, ano:int) -> None:
    livro:dict = {'titulo':titulo, 'autor':autor, 'ano':ano}
    for k, v in livro.items():
        print(f'{k}: {v}')

# Exercício 04
# Dicionários: Criar um dicionário que conte as ocorrências de cada caractere em uma string.
def exercicio_04(string:str) -> None:
    ocorrencias:dict = {}
    
    for char in string.lower():
        if char != ' ':
            ocorrencias[char] = ocorrencias.get(char, 0) + 1
    
    for k, v in ocorrencias.items():
        print(f'{k}: {v}')

# Listas: Calcule o preço total da lista de compras ["maçã", "banana", "cereja"] com preços [0.45, 0.30, 0.65]
def exercicio_05(items:list, precos:list) -> None:
    lista_compras:dict = dict(zip(items, precos))

    for k, v in lista_compras.items():
        print(f'{k}: {v}')

    total = sum(precos)
    print(f'Total: {total}')

if __name__ == '__main__':
    # exercicio_01()
    # exercicio_02()
    # exercicio_03('1984', 'George Orwell', 1949)
    # exercicio_04('O rato roeu a roupa do rei Raúl de Roma')
    # exercicio_05(['maçã', 'banana', 'cereja'], [0.45, 0.30, 0.65])
    ...
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

# Exercício 06
# Listas: Dada a lista de emails ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"], remover todos os duplicados.
def exercicio_06(emails:list) -> None:
    emails = list(set(emails))
    print(emails)

# Exercício 07
# Listas: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
def exercicio_07(idades:list) -> None:
    idades = [idade for idade in idades if idade >= 18]
    print(idades)

# Exercício 08
# Dicionários: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
def exercicio_08(pessoas:list) -> None:
    pessoas = sorted(pessoas, key=lambda pessoa: pessoa['nome'])
    print(pessoas)

# Exercício 09
# Listas: Dado um conjunto de números, calcule a média aritmética.
def exercicio_09(numeros:list) -> None:
    media:float = sum(numeros) / len(numeros)
    print('Média: ', media)

# Exercício 10
# Listas: Dividindo dados em grupos, Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
def exercicio_10(valores:list) -> None:
    pares:list = [num for num in valores if num % 2 == 0]
    impares:list = [num for num in valores if num % 2 != 0]
    print(f'Valores pares: {pares}\nValores ímpares: {impares}')

# Exercício 11
# Dicionários: Atualizando dados, dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
def exercicio_11(produtos:list, id:int, preco:float) -> None:
    for produto in produtos:
        if produto['id'] == id:
            print(f'\nProduto encontrado\nID: {produto["id"]}\nNome: {produto["nome"]}\nPreço: R$ {produto['preço']} \natualizando preço...\n')
            produto['preço'] = preco
    
    print('\nProdutos atualizados:')
    for i in produtos:
        print(i)

# Exercício 12
# Dicionários: Unindo dicionários, dados dois dicionários, fundi-los em um único dicionário.
def exercicio_12(d1:dict, d2:dict) -> None:
    d3:dict = {**d1, **d2}
    print(d3)

# Exercício 13
# Dicionários: Filtrando dados de um dicionário, dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
def exercicio_13(estoque:dict) -> None:
    estoque:dict = {k:v for k, v in estoque.items() if v > 0}
    print(estoque)

# Exercício 14
# Dicionários: Extraindo chaves e valores de um dicionário, dado um dicionário, criar listas separadas para suas chaves e valores. 
def exercicio_14(dicionario:dict) -> None:
    chaves:list = list(dicionario.keys())
    valores:list = list(dicionario.values())
    print(f'Chaves: {chaves}\nValores: {valores}')

# Exercício 15
# Dicionários: Dada uma string, contar a frequência de cada caractere usando um dicionário.
def exercicio_15(string:str) -> None:
    dicionario:dict = {}
    for char in string:
        if char not in dicionario:
            dicionario[char] = 1
        else:
            dicionario[char] += 1

    print(dicionario)

if __name__ == '__main__':
    # exercicio_01()
    # exercicio_02()
    # exercicio_03('1984', 'George Orwell', 1949)
    # exercicio_04('O rato roeu a roupa do rei Raúl de Roma')
    # exercicio_05(['maçã', 'banana', 'cereja'], [0.45, 0.30, 0.65])
    # exercicio_06(['user@example.com', 'admin@example.com', 'user@example.com', 'manager@example.com'])
    # exercicio_07([22, 15, 30, 17, 18])
    
    # exercicio_08([
    # {"nome": "Bob", "idade": 25},
    # {"nome": "Carol", "idade": 20},
    # {"nome": "Alice", "idade": 30}
    # ])
    
    # exercicio_09([10, 20, 30, 40, 50])
    # exercicio_10([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    # exercicio_11([
    # {"id": 1, "nome": "Teclado", "preço": 100},
    # {"id": 2, "nome": "Mouse", "preço": 80},
    # {"id": 3, "nome": "Monitor", "preço": 300}
    # ], 2, 90)
    
    # exercicio_12(
    #     d1={"a": 1, "b": 2},
    #     d2={"c": 3, "d": 4}
    # )
    
    # exercicio_13(estoque={"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0})

    # exercicio_14(dicionario={"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
    
    # exercicio_15('engenharia de dados')
    ...
"""
Crie uma classe Produto e implemente o método especial __str__ para 
representar o produto como uma string com nome e preço formatado.
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preco: R${self.preco:.2f}"

"""
Implemente um método especial __repr__ na classe Produto para que 
a representação da instância seja mais técnica, mostrando o tipo e os atributos.
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preco: R${self.preco:.2f}"

    def __repr__(self):
        return f"Produto('{self.nome}', {self.preco})"

"""
Crie uma classe Aluno e implemente o método __len__ 
para retornar o número de disciplinas que o aluno está matriculado.
"""

class Aluno:
    def __init__(self, nome, disciplinas):
        self.nome = nome
        self.disciplinas = disciplinas

    def __len__(self):
        return len(self.disciplinas)

"""
Implemente o método especial __add__ em uma classe Produto para 
permitir somar os preços de dois produtos.
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preco: R${self.preco:.2f}"

    def __add__(self, other):
        if not isinstance(other, Produto):
            raise TypeError("Você só pode somar produtos.")
        return self.preco + other.preco


"""
Implemente um método especial __eq__ na classe Produto
para comparar se dois produtos são iguais (considerando o mesmo nome e preço).
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preco: R${self.preco:.2f}"

    def __eq__(self, other):
        if not isinstance(other, Produto):
            return False
        return self.nome == other.nome and self.preco == other.preco

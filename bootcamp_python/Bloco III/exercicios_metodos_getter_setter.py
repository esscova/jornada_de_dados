import re


"""
Crie uma classe Produto com um atributo preco. 
Adicione um método getter e setter para acessar e modificar o preço, 
garantindo que o preço não seja negativo.
"""

class Produto:
    def __init__(self, preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        if preco < 0:
            raise ValueError("O preço deve ser maior ou igual a zero.")
        self.__preco = preco

"""
Implemente um getter e setter para o atributo nome de uma classe Pessoa. 
O setter deve garantir que o nome não contenha números ou caracteres especiais.
"""

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not re.match("^[A-Za-zÀ-ÿ ]+$", nome):
            raise ValueError("O nome deve conter apenas letras e espaços.")
    
        self.__nome = nome

"""
Crie uma classe ContaBancaria com um atributo saldo. 
Adicione métodos getter e setter para manipular o saldo, 
garantindo que o saldo nunca fique negativo.
"""

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("O saldo deve ser maior ou igual a zero.")
        self.__saldo = saldo

"""
Implemente um getter e setter para o atributo idade de uma classe Pessoa, 
onde o setter só deve permitir valores maiores que 0.
"""

class NovaPessoa(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome)
        self.__idade = idade

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade <= 0:
            raise ValueError("A idade deve ser maior que zero.")
        self.__idade = idade

"""
Crie uma classe Produto com um atributo quantidade. 
Adicione um método getter e setter para controlar a quantidade,
garantindo que ela não seja um valor negativo e que a quantidade mínima seja 1.
"""

class NovoProduto(Produto):
    def __init__(self, preco, quantidade):
        super().__init__(preco)
        self.__quantidade = quantidade

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade < 1:
            raise ValueError("A quantidade deve ser maior ou igual a um.")
        self.__quantidade = quantidade
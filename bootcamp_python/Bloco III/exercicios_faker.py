import faker
from loguru import logger
from typing import Tuple, Dict, List


"""
Crie uma classe GeradorDeDados que usa a biblioteca Faker para gerar um nome e um endereço aleatório.
"""

class GeradorDeDados:
    def __init__(self):
        self.fake = faker.Faker()

    def gerar_dados(self) -> Tuple[str, str]:
        """ 
        Gera um nome e um endereço aleatórios e retorna-os como uma tupla. 
        
        Returns:
            Tuple[str, str]: Uma tupla contendo o nome e o endereço.
        """
        logger.info("Gerando dados aleatórios...")
        nome:str = self.fake.name()
        endereco:str = self.fake.address()
        logger.info("Dados gerados com sucesso!")
        return nome, endereco

"""
Implemente um método na classe GeradorDeDados para gerar um e-mail falso com a ajuda do Faker.
"""
class GeradorDeDados:
    def __init__(self):
        self.fake = faker.Faker()

    def gerar_dados(self) -> Dict[str, str]:
        """ 
        Gera um nome, email e um endereço aleatórios. 
        
        Returns:
            Dict[str, str]: Um dicionário contendo o nome e o endereço.
        """

        logger.info("Gerando dados aleatórios...")
        
        nome:str = self.fake.name()
        endereco:str = self.fake.address()
        email:str = self.gerar_email()

        logger.info("Dados gerados com sucesso!")
        logger.info(f'nome: {nome}, email: {email}, endereco: {endereco}')
        
        return {
            "nome": nome,
            "endereco": endereco,
            "email": email}

    def gerar_email(self) -> str:
        return self.fake.email()

"""
Crie uma classe BancoDeDadosFalso que gera uma lista de 10 usuários com nome, idade e e-mail utilizando a biblioteca Faker.
"""
class BancoDeDadosFalso:
    def __init__(self):
        self.gerador = GeradorDeDados()

    def gerar_usuarios(self) -> list[Dict[str, str]]:
        """
        Gera uma lista de 10 usuários com nome, idade e e-mail utilizando a biblioteca Faker.

        Returns:
            list[Dict[str, str]]: Uma lista de dicionários contendo os usuários gerados.
        """
        return [self.gerador.gerar_dados() for _ in range(10)]

"""
Crie uma classe GeradorDeProdutos que usa o Faker para gerar um nome de produto, preço e descrição. Gere uma lista de 5 produtos fictícios.
"""

class GeradorDeProdutos:
    def __init__(self):
        self.fake = faker.Faker()

    def gerar_produtos(self) -> list[Dict[str, str]]:
        """
        Gera uma lista de 5 produtos fictícios.

        Returns:
            list[Dict[str, str]]: Uma lista de dicionários contendo os produtos gerados.
        """
        logger.info("Gerando produtos...")
       
        produtos:List[Dict[str, str]] = [
            {
            'item': self.fake.word(),
            'descricao': self.fake.text(),
            'preco': self.fake.random_number(digits=2)
            }for _ in range(5)
        ]
        
        logger.info("Produtos gerados com sucesso!")
        return produtos

"""
Implemente uma classe GeradorDeVendas que cria dados de vendas, como o nome do cliente, o produto adquirido e a data da venda, utilizando o Faker.
"""
class GeradorDeVendas:
    def __init__(self):
        self.fake = faker.Faker()

    def gerar_vendas(self) -> list[Dict[str, str]]:
        """
        Gera uma lista de 5 vendas fictícios.

        Returns:
            list[Dict[str, str]]: Uma lista de dicionários contendo as vendas geradas.
        """
        logger.info("Gerando vendas...")
        vendas:List[Dict[str, str]] = [
            {
            'cliente': self.fake.name(),
            'produto': self.fake.word(),
            'data': self.fake.date()
            }for _ in range(5)
        ]
        
        logger.info("Vendas geradas com sucesso!")
        return vendas


def main():
    # GeradorDeDados().gerar_dados() # teste gerador de dados
    # BancoDeDadosFalso().gerar_usuarios() # teste gerador de usuarios
    # for i in GeradorDeProdutos().gerar_produtos(): # teste gerador de produtos
    for i in GeradorDeVendas().gerar_vendas(): # teste gerador de vendas
        print(i)

if __name__ == "__main__":
    main()
    
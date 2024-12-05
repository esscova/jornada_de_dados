import os
import csv
from faker import Faker
from loguru import logger

faker = Faker()

class GerarCSV:
    def __init__(self):
        self.produtos = []
        self.file_path = None
        
    def gerar_produtos(self, nome_arquivo:str='dados_produtos.csv', quantidade_registros:int=100):
        """
        Função para gerar dados de produtos e salvar em um arquivo CSV com campos: id, nome, preco, estoque.

        Args:
            nome_arquivo = String para nomear arquivo gerado, por default 'dados_produtos.csv'
            quantidade_registros = Inteiro com a quantidade de registros a serem gerados, 100 registros por default.
            
        Returns:
            Um arquivo CSV em uma pasta chamada 'data' um nível acima.
            
        """
        pasta = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

        if not os.path.exists(pasta):
            os.makedirs(pasta)

        self.file_path = os.path.join(pasta, nome_arquivo)
        
        try:
            logger.info('Iniciando arquivo CSV')
            with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
                fieldnames = ['id', 'nome', 'preco', 'estoque']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                logger.info('Gerando registros...')
                self.produtos = [
                    {
                        'id': i + 1, 
                        'nome': faker.name(),
                        'preco': round(faker.pyfloat(left_digits=2, right_digits=2, positive=True), 2),
                        'estoque': faker.pyint(min_value=1, max_value=100)
                    } 
                    for i in range(quantidade_registros)
                ]
                writer.writerows(self.produtos)
                
            logger.info(f'Arquivo de produtos gerado com sucesso: {self.file_path}')
            return self.file_path
            
        except Exception as e:
            logger.error(f'Erro ao gerar arquivo de produtos. {e}')
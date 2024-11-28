import csv
import os
import json
from faker import Faker
from loguru import logger

class FileGenerator:
    """Classe responsável por gerar arquivos com dados fictícios."""
    
    def __init__(self, log_path: str):
        """
        Inicializa a classe com configuração de logger e gerador de dados fictícios.

        Args:
            log_path (str): Caminho para o arquivo de log.
        """
        # Configuração do logger
        self.setup_logger(log_path)
        
        # Gerador de dados
        self.fake = Faker()
        Faker.seed(42)

    @staticmethod
    def setup_logger(log_path: str):
        """
        Configura o logger.

        Args:
            log_path (str): Caminho para o arquivo de log.
        """
        logger.add(log_path, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
    
    @staticmethod
    def create_directory(file_path: str):
        """
        Cria o diretório necessário para salvar o arquivo, se não existir.

        Args:
            file_path (str): Caminho completo do arquivo.
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    def generate_csv(self, file_path: str, num_records: int):
        """
        Gera um arquivo CSV com dados fictícios:
            - ID
            - Nome
            - Endereço
            - Email
        Args:
            file_path (str): O caminho onde o arquivo CSV será salvo.
            num_records (int): O número de registros a serem gerados.
        """
        try:
            self.create_directory(file_path)
            with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
                logger.info('Gerando arquivo CSV ...')
                fields = ['ID','Nome', 'Endereço', 'Email']
                writer = csv.DictWriter(csv_file, fieldnames=fields)
                writer.writeheader()

                logger.info('Escrevendo registros no CSV ...')
                for _ in range(num_records):
                    writer.writerow({
                        'ID': _ + 1,
                        'Nome': self.fake.name(),
                        'Endereço': self.fake.address().replace('\n', ', '),
                        'Email': self.fake.email()
                    })
                logger.info(f'Arquivo {file_path} gerado com sucesso com {num_records} registros.')
        except Exception as e:
            logger.error(f'Erro ao gerar arquivo CSV: {e}')

    def generate_json(self, file_path: str, num_records: int):
        """
        Gera um arquivo JSON com dados fictícios.
            - ID
            - Companhia
            - Valor

        Args:
            file_path (str): O caminho onde o arquivo JSON será salvo.
            num_records (int): O número de registros a serem gerados.
        """
        try:
            self.create_directory(file_path)
            with open(file_path, 'w', encoding='utf-8') as json_file:
                logger.info('Gerando arquivo JSON ...')
                data = [
                    {
                        'ID': i + 1,
                        'Companhia': self.fake.company().capitalize(),
                        'Valor': self.fake.random_int(min=1, max=1000)
                    }
                    for i in range(num_records)
                ]
                json.dump(data, json_file, indent=4, ensure_ascii=False)
                logger.info(f'Arquivo {file_path} gerado com sucesso com {num_records} registros.')
        except Exception as e:
            logger.error(f'Erro ao gerar arquivo JSON: {e}')

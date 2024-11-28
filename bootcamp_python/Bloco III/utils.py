import csv
import os
import json
from faker import Faker
from loguru import logger

class FileGenerator:
    """Classe responsável por gerar arquivos com dados fictícios."""
    
    def __init__(self, output_dir: str = 'data', log_file: str = 'log.txt'):
        """
        Inicializa a classe com configuração de logger, diretório de saída e gerador de dados fictícios.

        Args:
            output_dir (str): Diretório onde os arquivos serão salvos. Padrão: 'data'.
            log_file (str): Nome do arquivo de log. Padrão: 'log.txt'.
        """
        # Diretório base: onde o script está localizado
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Diretório de saída absoluto
        self.output_dir = os.path.join(self.base_dir, output_dir)
        os.makedirs(self.output_dir, exist_ok=True)  
        
        # Configuração do logger
        self.log_path = os.path.join(self.output_dir, log_file)
        self.setup_logger(self.log_path)
        
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

    def generate_csv(self, file_name: str, num_records: int):
        """
        Gera um arquivo CSV com dados fictícios:
            - ID
            - Nome
            - Endereço
            - Email

        Args:
            file_name (str): Nome do arquivo (sem extensão).
            num_records (int): Quantidade de registros a serem gerados.
        """
        file_path = os.path.join(self.output_dir, f"{file_name}.csv")
        try:
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

    def generate_json(self, file_name: str, num_records: int):
        """
        Gera um arquivo JSON com dados fictícios:
            - ID
            - Companhia
            - Valor

        Args:
            file_name (str): Nome do arquivo (sem extensão).
            num_records (int): Quantidade de registros a serem gerados.
        """
        file_path = os.path.join(self.output_dir, f"{file_name}.json")
        try:
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

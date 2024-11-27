import csv
import os
import json
from faker import Faker
from loguru import logger

# configuração do logger
logger.add('data/log_utils.txt', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
# gerador de dados
fake = Faker()
Faker.seed(42)

def gerar_arquivo_csv(caminho_arquivo: str, num_linhas: int) -> None:
    """Gera um arquivo CSV com dados fictícios.

    Args:
        caminho_arquivo (str): O caminho onde o arquivo CSV será salvo.
        num_linhas (int): O número de registros a serem gerados.
    """
    try:
        # cria um diretorio se nao existir
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)

        with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            logger.info('Gerando arquivo csv ...')
            campos = 'Nome Endereço Email'.split()
            writer = csv.DictWriter(arquivo_csv, fieldnames=campos)
            writer.writeheader()

            logger.info('Escrevendo registros no csv ...')
            for _ in range(num_linhas):
                writer.writerow({
                    'Nome': fake.name(),
                    'Endereço': fake.address().replace('\n', ', '),  # Substitui nova linha por vírgula
                    'Email': fake.email()
                })
            logger.info(f'Arquivo {caminho_arquivo} gerado com sucesso com {num_linhas} registros.')

    except Exception as e:
        logger.error(f'Erro ao gerar arquivo csv: {e}')

def gerar_arquivo_json(caminho_arquivo: str, num_linhas: int) -> None:
    """Gera um arquivo JSON com dados fictícios.

    Args:
        caminho_arquivo (str): O caminho onde o arquivo CSV será salvo.
        num_linhas (int): O número de registros a serem gerados.
    """
    try:
        # cria um diretorio se nao existir
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)

        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_json:
            logger.info('Gerando arquivo json ...')
            dados = []
            for _ in range(num_linhas):
                dados.append({
                    'ID': _ + 1,
                    'Companhia': fake.company().capitalize(),
                    'Valor': fake.random_int(min=1, max=1000)
                })
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
            logger.info(f'Arquivo {caminho_arquivo} gerado com sucesso com {num_linhas} registros.')

    except Exception as e:
        logger.error(f'Erro ao gerar arquivo json: {e}')



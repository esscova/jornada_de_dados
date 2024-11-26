"""
Desafio 1: Monitoramento de um Pipeline de ETL
Você precisa monitorar um pipeline de ETL que processa múltiplos arquivos CSV e os consolida em um único arquivo.
Adicione logs para acompanhar o progresso do pipeline, identificar erros e registrar o tempo total de execução.

Tarefas:

Leia três arquivos CSV fictícios, combine-os em um único DataFrame e salve o resultado.
Adicione logs para:
Registrar o início e o término de cada etapa.
Capturar exceções, como arquivos ausentes ou problemas de leitura.
Registrar o tempo total de execução.
Requisitos:

Use rotação de arquivos de log baseada no tamanho (ex: 1 MB).
Retenha logs apenas por 7 dias.
Dicas:

Use logger.add() para configurar a rotação e retenção de logs.
Utilize try/except com logger.exception para capturar erros.
"""
import os
import glob
import csv
from loguru import logger

def carregar_dados(diretorio:str) -> list:
    logger.add('pipeline.log',
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | <level> {message} </level>",
               rotation='1 MB',
               retention='7 days',
               compression='zip')

    try:
        logger.info(f'Buscando arquivos CSV no diretório: {diretorio}')
        logger.info('Etapa: Carregando dados...')
        arquivos_csv = glob.glob(os.path.join(diretorio, '*.csv'))
        logger.info(f'{len(arquivos_csv)} : arquivos CSV encontrados.')
        
        if not arquivos_csv:
            logger.error('Nenhum arquivo CSV encontrado.')
            return []

        dados:list = []
        for arquivo in arquivos_csv:
            with open(arquivo, 'r', newline='') as file:
                leitor = csv.DictReader(file)
                for linha in leitor:
                    dados.append(linha)

        logger.info('Dados carregados com sucesso.')
        return dados

    except Exception as e:
        logger.exception(f'Erro ao carregar dados: {e}')
        return []
    
def main() -> None:
    caminho_diretorio:str = 'data/'
    dados = carregar_dados(caminho_diretorio)
    for i in dados:
        print(i)

if __name__ == '__main__':
    main()
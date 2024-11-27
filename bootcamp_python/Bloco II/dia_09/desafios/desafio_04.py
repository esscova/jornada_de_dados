"""

Desafio 4: Integração com pandas
Você está trabalhando em um relatório que carrega, limpa e exporta dados usando a biblioteca pandas. 
O objetivo é monitorar cada etapa e capturar qualquer erro gerado pelo pandas.

Tarefas:
[] Integre os logs do pandas ao Loguru para capturar qualquer erro gerado.
[] Carregue um arquivo CSV fictício, 

aplique as seguintes etapas de limpeza:
    - Remova colunas duplicadas.
    - Renomeie colunas.
    - Elimine linhas com valores ausentes.

[] Registre o progresso e os resultados da limpeza:
    - Número de linhas e colunas antes e depois da limpeza.
    - Tempo total de execução.

Requisitos:
Implemente um InterceptHandler para redirecionar os logs do pandas.
Adicione logs detalhados antes e depois de cada etapa de limpeza.

Dicas:
Use logger.debug para registrar informações detalhadas (ex: DataFrame.head()).

"""

import pandas as pd
from loguru import logger
import logging
import time

logger.add('sistema.log', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="DEBUG")

class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger.opt(depth=6).log(record.levelno, record.getMessage())

logging.basicConfig(handlers=[InterceptHandler()], level=logging.DEBUG)
logging.getLogger('pandas').setLevel(logging.DEBUG)

def carregar_dados(caminho):
    logger.info(f"Carregando dados do arquivo: {caminho}")
    return pd.read_csv(caminho, sep=',', encoding='utf-8')

def remover_colunas_duplicadas(df):
    logger.info("Removendo colunas duplicadas...")
    df = df.T.drop_duplicates().T
    return df

def renomear_colunas(df):
    logger.info("Renomeando colunas...")
    df.columns = [f"coluna_{i}" for i in range(len(df.columns))]
    return df

def preencher_valores_ausentes(df, valor=0):
    logger.info("Preenchendo valores ausentes...")
    df.fillna(valor, inplace=True)
    return df

def exportar_dados(df, caminho_saida):
    logger.info(f"Exportando dados para {caminho_saida}...")
    df.to_csv(caminho_saida, index=False)

def main():
    try:
        start_time = time.time()
        
        caminho_entrada = 'data/example.csv'
        caminho_saida = 'data/example_cleaned.csv'
        
        df = carregar_dados(caminho_entrada)
        logger.debug(f'Dados carregados:\n{df.head()}')

        logger.debug(f'Dimensão inicial: {df.shape}')
        
        df = remover_colunas_duplicadas(df)
        logger.debug(f'Dados após remoção de colunas duplicadas:\n{df.head()}')

        df = renomear_colunas(df)
        logger.debug(f'Colunas renomeadas:\n{df.head()}')

        df = preencher_valores_ausentes(df, valor=0)
        logger.debug(f'Valores ausentes preenchidos:\n{df.head()}')

        logger.debug(f'Dimensão final: {df.shape}')
        
        end_time = time.time()
        logger.info(f"Limpeza concluída em {end_time - start_time:.2f} segundos.")

        exportar_dados(df, caminho_saida)
        logger.info("Dados exportados com sucesso.")

    except Exception as e:
        logger.critical(f"Erro ao processar os dados: {e}")

if __name__ == "__main__":
    main()

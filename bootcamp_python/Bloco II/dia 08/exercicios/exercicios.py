"""

descrição: 
    - dia 08 bootcamp python: Funções 
    - Realizar uma ETL (Extract, Transform, Load) simples utilizando Python e a biblioteca Pandas, Json e Parquet.
autor: 
    - wellington moreira
    - wsantos08@hotmail.com

versão python: 
    - 3.12.4

created: 2024-11-22

"""

import os
import glob
import pandas as pd

# Extract: Ler os dados de um arquivo JSON e concatenar os dados extraídos em um único DataFrame
def extrair_dados_json(caminho_arquivo:str) -> pd.DataFrame:
    try:
        print(f'\nExtraindo dados de {caminho_arquivo}\n')
        arquivos_json = glob.glob(os.path.join(caminho_arquivo, '*.json'))
        print(f'\nArquivos JSON encontrados: {len(arquivos_json)}\n')
        
        if not arquivos_json:
            raise FileNotFoundError(f'Nenhum arquivo JSON encontrado na pasta {caminho_arquivo}')
        
        dados = [ pd.read_json(arquivo) for arquivo in arquivos_json ]
        
        return pd.concat(dados, ignore_index=True)
    
    except ValueError as e:
        print(f'Erro ao extrair dados: {e}')
        return None

#Transform:  aplicar uma transformação nos dados extraidos, criando coluna receita com o produto vezes a quantidade vendida.
def transformar_dados(dados:pd.DataFrame) -> pd.DataFrame:
    try:
        print('Transformando dados...')
        if 'Quantidade' not in dados.columns or 'Venda' not in dados.columns:
            raise KeyError('Colunas "Quantidade" e "Venda" nao encontradas no DataFrame')
        dados['Receita'] = dados['Quantidade'] * dados['Venda']
        print('Dados transformados com sucesso')
        return dados
    
    except KeyError as e:
        print(f'Erro ao transformar dados: {e}')
        return None

#Load: Salvar o DataFrame resultante em um arquivo CSV ou PARQUET.
def salvar_dados(dados:pd.DataFrame, caminho_arquivo:str, formato:list) -> None:
    try:
        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError(f'Pasta {caminho_arquivo} nao encontrada')
        
        if 'csv' in formato:
            dados.to_csv(os.path.join(caminho_arquivo, 'dados_transformados.csv'), index=False)
        
        if 'parquet' in formato:
            dados.to_parquet(os.path.join(caminho_arquivo, 'dados_transformados.parquet'))

        print(f'Dados salvos com sucesso em {caminho_arquivo}')
    
    except ValueError as e:
        print(f'Erro ao salvar dados: {e}')

if __name__ == '__main__':
    pasta = 'data'
    dados = extrair_dados_json(caminho_arquivo=pasta)
    dados_novos=transformar_dados(dados=dados)
    salvar_dados(dados=dados_novos, caminho_arquivo=pasta, formato=['csv', 'parquet'])
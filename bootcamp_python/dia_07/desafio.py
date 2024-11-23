"""
descrição: 
    - Desafio dia 07 bootcamp python: Funções
    - Análise de vendas de produtos

autor:
    - wellington moreira
    - wsantos08@hotmail.com

versao python: 
    - 3.12.4

"""

import csv
from typing import List, Dict
from collections import defaultdict

# função para leitura do csv
def ler_arquivo_csv(caminho_arquivo:str) -> List[dict]:
    """
    Função para ler o arquivo csv, recebe um caminho de arquivo e 
    retorna uma lista de dicionários.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            return list(leitor_csv)

    except Exception as e:
        print(f'Erro: {e}')

    except FileNotFoundError:
        print(f'Arquivo {caminho_arquivo} não encontrado')

# função para processar os dados do dicionário onde,
# a chave seja a categoria e o valor é uma lista de dicionários, 
# cada um contendo informações do produto (Produto, Quantidade, Venda)

def processar_dados(dados:List[dict]) -> Dict[str, List[dict]]:
    """
    Função para processar os dados do dicionário onde,
    a chave seja a categoria e o valor é uma lista de dicionários, 
    cada um contendo informações do produto (Produto, Quantidade, Venda)
    """
    categorias:Dict[str, List[dict]] = defaultdict(list)

    for item in dados:
        categoria = item['Categoria']
        categorias[categoria].append({
            'Produto': item['Produto'],
            'Quantidade': int(item['Quantidade']),
            'Venda': float(item['Venda'])
        })

    return dict(categorias)

# função para calcular o total de vendas por categoria
def calcular_total_vendas(categorias:Dict[str, List[dict]]) -> Dict[str, float]:
    """
    Função para calcular o total de vendas por categoria, retorna um dicionário.
    """
    total_vendas:Dict[str, float] = {}

    for categoria, produtos in categorias.items():
        total_vendas[categoria] = sum([produto['Venda'] for produto in produtos])

    return total_vendas


# função principal
def main() -> None:
    # extração
    caminho_arquivo:str = 'vendas.csv'
    vendas:List[dict] = ler_arquivo_csv(caminho_arquivo)
    
    # transformação
    categorias = processar_dados(vendas)

    # análise
    total_vendas_por_categoria = calcular_total_vendas(categorias)

    # apresentação
    print(total_vendas_por_categoria)

if __name__ == '__main__':
    main()
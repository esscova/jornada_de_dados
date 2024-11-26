"""
Desafio 2: Rastreamento de Erros em Transformações de Dados
Você está processando um DataFrame com transformações complexas (normalização de colunas, preenchimento de valores ausentes, etc.). 
Às vezes, erros ocorrem em determinadas etapas, mas você não sabe onde exatamente.

Tarefas:

Crie um DataFrame fictício com valores ausentes e dados inconsistentes.
Aplique as seguintes transformações:
Preencha valores ausentes com a média da coluna.
Normalize os valores entre 0 e 1.
Converta uma coluna de strings para números inteiros.
Adicione logs para identificar o início e término de cada transformação.
Registre erros específicos com rastreamento completo da pilha.
Requisitos:

Use @logger.catch para capturar erros em funções específicas.
Adicione variáveis no log para indicar o número de linhas processadas antes de cada etapa.
Dicas:

Experimente introduzir erros propositais, como valores inválidos, para testar os logs.

"""
import pandas as pd
from loguru import logger


dados = pd.DataFrame({
    'coluna1': [1, 2, 3, None, 'eh vero'],
    'coluna2': ['a', 'b', 'c', 'd', 'Maledeto Mezenga'],
    'coluna3': [10, 20, 30, 40, 5000]     
})


@logger.catch   
def main():
    # media coluna 1
    media = dados['coluna1'].mean()
    dados['coluna1'].fillna(media, inplace=True)

    # min max normalizador
    dados['coluna3'] = (dados['coluna3'] - dados['coluna3'].min()) / (dados['coluna3'].max() - dados['coluna3'].min())

    # string pra inteiro
    dados['coluna2'] = dados['coluna2'].astype(int)

if __name__ == '__main__':
    main()
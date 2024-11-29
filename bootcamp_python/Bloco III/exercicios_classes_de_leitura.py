import csv
import os
from loguru import logger
from typing import List, Dict, Optional
from abc import ABC, abstractmethod
import json

"""

Crie uma classe LeitorCSV que leia um arquivo CSV e permita filtrar os dados por um valor específico em uma coluna.

"""
class LeitorCSV(ABC):
    def __init__(self, caminho_arquivo:str):
        self.caminho_arquivo = caminho_arquivo
        self.data = None

    def fetch_csv(self) -> Optional[List[Dict[str, str]]]:
        """
        
        Ler o arquivo CSV e armazenar os dados em uma lista de dicionários.

        """
        
        try:
            logger.info(f'Lendo o arquivo {self.caminho_arquivo}')
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:
                self.data = list(csv.DictReader(arquivo_csv))
                logger.info('Arquivo lido com sucesso')
                return self.data
    
        except Exception as e:
            logger.error(f'Erro ao ler o arquivo {self.caminho_arquivo}: {e}')
            return None

        except FileNotFoundError:
            logger.error(f'Arquivo {self.caminho_arquivo} nao encontrado')
            return None

    def filter_by_column(self, col:str, value:str) -> List[Dict[str, str]]:
        """

        Filtrar os dados de um arquivo CSV por um valor em uma coluna específica.

        Returns:
            List[Dict[str, str]]: Lista de dicionários contendo os dados filtrados.

        """
        logger.debug(f'coluna {col}, valor {value}')
        result:List[Dict[str, str]] = [item for item in self.data if item[col] == value]
        
        if not result:
            logger.info(f'Nenhum valor encontrado na coluna {col} com o valor {value}')
        
        logger.debug(result)
        return result
    
    @abstractmethod
    def filter_by_columns(self, col1:str, value1:str, col2:str, value2:str) -> List[Dict[str, str]]:
        pass

    @abstractmethod
    def order_by_column(self, col:str) -> List[Dict[str, str]]:
        pass

    @abstractmethod
    def save_filtered_data(self, caminho_arquivo:str, data:List[Dict[str, str]]):
        pass

"""

Modifique a classe LeitorCSV para filtrar dados de um arquivo CSV com base em múltiplos atributos. Por exemplo, filtrar por "nome" e "idade".

"""

class LeitorCSV2(LeitorCSV):
    def filter_by_columns(self, col1:str, value1:str, col2:str, value2:str) -> List[Dict[str, str]]:
        """
        Filtrar os dados de um arquivo CSV com base em duas colunas e seus respectivos valores.

        Returns:
            List[Dict[str, str]]: Lista de dicionários contendo os dados filtrados.
        """
        if not self.data:
            logger.error('Nao foi possivel filtrar, dados nao carregados')
            return None

        logger.debug(f'coluna {col1}, valor {value1}')
        logger.debug(f'coluna {col2}, valor {value2}')
        result:List[Dict[str, str]] = [item for item in self.data if item[col1] == value1 and item[col2] == value2]
        
        if not result:
            logger.info(f'Nenhum valor encontrado nas colunas {col1} e {col2} com os valores {value1} e {value2}')
        
        logger.debug(result)
        return result

"""

Implemente um método na classe LeitorCSV que permita ordenar os dados de um arquivo CSV com base em uma coluna específica.

"""
class LeitorCSV3(LeitorCSV2):
    def order_by_column(self, col:str) -> List[Dict[str, str]]:
        """

        Ordenar os dados de um arquivo CSV com base em uma coluna especifica.

        Returns:    
            List[Dict[str, str]]: Lista de dicionários contendo os dados ordenados.
        
        """
        
        if not self.data:
            logger.error('Nao foi possivel filtrar, dados nao carregados')
            return None

        logger.info(f'Ordenando dados por coluna: "{col}"')        
        result:List[Dict[str, str]] = sorted(self.data, key=lambda item: item[col])
        
        if not result:
            logger.warning(f'Nenhum valor encontrado na coluna {col}')
        
        logger.info('Dados ordenados com sucesso')
        return result

"""

Crie uma classe LeitorJSON que leia um arquivo JSON e permita filtrar os dados por um valor em um campo específico.

"""

class LeitorJSON:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.dados = None

    def fetch_json(self) -> Optional[List[Dict[str, str]]]:
        """
        Ler um arquivo JSON.
        """
        try:
            logger.info('Lendo o arquivo JSON...')
            logger.debug(f'arquivo: "{self.caminho_arquivo}"')
            
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo_json:
                self.dados = json.load(arquivo_json)
                logger.info('Arquivo lido com sucesso')
                return self.dados

        except Exception as e:
            logger.error(f'Erro ao ler o arquivo {self.caminho_arquivo}: {e}')
            return None
        except FileNotFoundError:
            logger.error(f'Arquivo {self.caminho_arquivo} nao encontrado')
            return None
        except json.JSONDecodeError:
            logger.error(f'Erro ao decodificar o arquivo JSON {self.caminho_arquivo}')
            return None

    def filter_by_key(self, key:str, value:str) -> List[Dict[str, any]]:
        """
        Filtrar os dados de um arquivo JSON com base em um valor em um campo específico.

        Returns:
            List[Dict[str, str]]: Lista de dicionários contendo os dados filtrados.
        
        """
        logger.debug(f'chave {key}, valor {value}')
        logger.info('Filtrando dados...')

        result:List[Dict[str, any]] = [item for item in self.dados if item[key] == value]
        
        if not result:
            logger.info(f'Nenhum valor encontrado na coluna {key} com o valor {value}')
        
        logger.info('Dados filtrados com sucesso')
        logger.debug(result)
        
        return result

"""

Implemente uma classe LeitorCSV que permita filtrar e salvar os dados filtrados em um novo arquivo CSV.

"""

class LeitorCSV4(LeitorCSV3):
    def save_filtered_data(self, caminho_arquivo:str, data:List[Dict[str, str]]):

        if os.path.exists(caminho_arquivo):
            logger.warning(f'O arquivo {caminho_arquivo} já existe. Ele será sobrescrito.')
        
        logger.info('Salvando dados filtrados...')
        logger.debug(f'Salvando dados filtrados em: "{caminho_arquivo}"')
        
        try:
            with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
                writer = csv.DictWriter(arquivo_csv, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

            logger.info('Dados salvos com sucesso')
        
        except Exception as e:
            logger.error(f'Erro ao salvar os dados: {e}')
        

if __name__ == '__main__':

    leitor_csv = LeitorCSV4('data/arquivo.csv')
    leitor_csv.fetch_csv()
    data = leitor_csv.filter_by_column('ID', '8')
    leitor_csv.save_filtered_data('data/novo_arquivo.csv', data)
"""

Criando Classes para Leitura de Arquivos

Exercício 1:
Crie uma classe LeitorTXT que recebe um caminho de arquivo como parâmetro e imprime o conteúdo do arquivo. 
Crie um arquivo de teste e utilize a classe para ler esse arquivo.

Exercício 2:
Modifique a classe LeitorTXT para incluir um método que conta o número de linhas no arquivo. Teste a classe com diferentes arquivos.

Exercício 3:
Crie uma classe LeitorCSV que utiliza a biblioteca csv para ler um arquivo CSV e imprime os dados de cada linha. Teste com um arquivo CSV de exemplo.

Exercício 4:
Implemente um método na classe LeitorCSV para buscar um valor específico em uma coluna do arquivo CSV. Teste com um arquivo que tenha várias colunas.

Exercício 5:
Crie uma classe LeitorJSON que leia um arquivo JSON e extraia informações específicas do arquivo, como um nome ou id. Teste com um arquivo JSON de exemplo.


"""
from loguru import logger
import csv
import json

logger.add('data/log.log', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

# Exercício 1
class LeitorTXT:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def ler_arquivo(self):
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                logger.info(f'Arquivo {self.caminho_arquivo} lido com sucesso')
                conteudo = arquivo.read()
                print(conteudo)

        except Exception:
            logger.error(f'Arquivo {self.caminho_arquivo} nao encontrado')

# Exercício 2
class LeitorTXT:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.linhas = 0

    def ler_arquivo(self):
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                logger.info(f'Arquivo {self.caminho_arquivo} lido com sucesso')
                conteudo = arquivo.read()
                self.linhas = len(conteudo.split('\n'))
                print(conteudo)

        except Exception:
            logger.error(f'Arquivo {self.caminho_arquivo} nao encontrado')
    
    def contar_linhas(self):
        logger.info(f'Arquivo {self.caminho_arquivo} possui {self.linhas} linhas')
        return self.linhas

# Exercício 3
class LeitorCSV:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def ler_arquivo(self):
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                logger.info(f'Arquivo {self.caminho_arquivo} lido com sucesso')
                leitor_csv = csv.DictReader(arquivo)
                for linha in leitor_csv:
                    print(linha)

        except Exception:
            logger.error(f'Arquivo {self.caminho_arquivo} nao encontrado')


# Exercício 4
class LeitorCSV:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.arquivo_csv = None

    def ler_arquivo(self):
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                logger.info(f'Arquivo {self.caminho_arquivo} lido com sucesso')
                self.arquivo_csv = list(csv.DictReader(arquivo))
                for linha in self.arquivo_csv:
                    print(linha)

        except Exception:
            logger.error(f'Arquivo {self.caminho_arquivo} nao encontrado')
    
    def buscar_dados(self, coluna, valor):
        
        logger.debug(f'Pesquisando por {valor} na coluna {coluna} do arquivo {self.caminho_arquivo}')
        logger.info('Buscando dados...')

        try:
            if len(coluna) == 0 or len(valor) == 0:
                logger.debug(f'coluna {coluna} ou valor {valor} vazios')
                logger.error('Coluna ou valor vazios')
                raise ValueError('Coluna ou valor vazios')
            
            for linha in self.arquivo_csv:
                if linha[coluna] == valor:
                    logger.debug(f'Valor {valor} encontrado na coluna {coluna} do arquivo {self.caminho_arquivo}')
                    print(linha)

        except Exception:
            logger.error(f'Arquivo {self.caminho_arquivo} nao encontrado')

# Exercício 5
class LeitorJSON:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.dados = None

    def ler_arquivo(self):
        logger.info('Lendo arquivo JSON...')
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                logger.debug(f'Arquivo {self.caminho_arquivo} lido com sucesso')
                self.dados = json.load(arquivo)
                print(self.dados)

        except FileNotFoundError:
            logger.error(f'Arquivo {self.caminho_arquivo} não encontrado')
        except json.JSONDecodeError:
            logger.error(f'Erro ao decodificar o arquivo JSON {self.caminho_arquivo}')
        except Exception as e:
            logger.error(f'Erro ao ler o arquivo {self.caminho_arquivo}: {e}')

    def buscar_dados(self, coluna, valor) -> list:
        logger.info('Buscando dados...')
        
        if self.dados is None:
            logger.error('Arquivo JSON nao carregado')
            return []

        try:
            if len(coluna) == 0:
                logger.debug(f'coluna {coluna} com campos vazios')
                logger.error('Coluna sem valores')
                raise ValueError('Coluna sem valores')

            logger.debug(f'Pesquisando por {valor} na coluna {coluna} do arquivo {self.caminho_arquivo}')

            resultados = [dado for dado in self.dados if coluna in dado and dado[coluna] == valor]

            if not resultados:
                logger.info(f'Valor {valor} nao encontrado na coluna {coluna} do arquivo {self.caminho_arquivo}')
            
            logger.info(f'Valores encontrados: {resultados}')
            
            return resultados

        except KeyError:
            logger.error(f'A coluna {coluna} não existe nos dados.')
        except Exception as e:
            logger.error(f'Erro ao buscar dados: {e}')

if __name__ == '__main__':

    leitor = LeitorTXT('data/arquivo.txt')
    leitor.ler_arquivo()
    leitor.contar_linhas()

    from utils import FileGenerator
    log_path = 'data/log.txt'
    caminho_arquivo_csv = 'data/arquivo.csv'

    file_generator = FileGenerator(log_path)
    file_generator.generate_csv('data/arquivo.csv', 10)

    num_linhas = 10

    leitor = LeitorCSV(caminho_arquivo_csv)
    leitor.ler_arquivo()
    leitor.buscar_dados('Email', 'jrice@example.org')

    caminho_arquivo_json = 'data/arquivo.json'
    file_generator.generate_json('data/arquivo.json', 10)

    leitor_json = LeitorJSON(caminho_arquivo_json)
    leitor_json.ler_arquivo()
    leitor_json.buscar_dados('ID', 8)
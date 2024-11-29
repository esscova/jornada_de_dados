"""
Crie uma classe abstrata FormaGeometrica com um método abstrato area().
Depois, crie duas subclasses: Circulo e Retangulo, que implementam o método area().
"""

from abc import ABC, abstractmethod
from loguru import logger
from math import pi
import csv
import json
from typing import List, Dict

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        """Calcula a area da forma geometrica"""
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self) -> float:
        """Calcula a area do circulo"""
        if not isinstance(self.raio, (int, float)):
            logger.error("Raio deve ser um número.")
            raise ValueError("Raio deve ser um número.")

        if self.raio < 0:
            logger.error("Raio deve ser um número positivo.")
            raise ValueError("Raio deve ser um número positivo.")

        logger.info("Calculando area do circulo...")

        try:
            area:float = pi * (self.raio ** 2)
            logger.info(f"Área do circulo: {area}")

        except Exception as e:
            logger.critical(f"Erro ao calcular área do círculo: {e}")
            raise Exception(f"Erro ao calcular área do círculo: {e}")

        return area
        

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        """Calcula a area do retangulo"""

        if not isinstance(self.largura, (int, float)) or not isinstance(self.altura, (int, float)):
            logger.error("Largura e altura devem ser um número.")
            raise ValueError("Largura e altura devem ser um número.")

        if self.largura <= 0 or self.altura <= 0:
            logger.error("Largura e altura devem ser maiores que zero.")
            raise ValueError("Largura e altura devem ser maiores que zero.")

        
        logger.info("Calculando area do retangulo...")        

        try:
            area:float = self.largura * self.altura
            logger.info(f"Área do retângulo: {area}")

        except Exception as e:
            logger.critical(f"Erro ao calcular área do retângulo: {e}")
            raise Exception(f"Erro ao calcular área do retângulo: {e}")

        return area

"""
Implemente uma classe abstrata Animal com um método abstrato fazer_som().
Crie duas subclasses: Cachorro e Gato, 
que implementam o método fazer_som() com sons diferentes.
"""

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        """Faz o som do animal"""
        pass

class Cachorro(Animal):
    def fazer_som(self) -> str:
        """Faz o som do cachorro"""
        logger.info("Fazendo som do cachorro...")
        return "Au au"

class Gato(Animal):    
    def fazer_som(self) -> str:
        """Faz o som do gato"""
        logger.info("Fazendo som do gato...")
        return "Miau"

"""
Crie uma classe abstrata Arquivo com um método abstrato ler(). 
Em seguida, crie duas subclasses: LeitorCSV e LeitorJSON, 
que implementam o método ler() de maneiras diferentes.
"""

class Arquivo(ABC):
    def __init__(self, caminho_arquivo:str):
        self.caminho_arquivo = caminho_arquivo
    @abstractmethod
    def ler(self):
        """Ler o arquivo"""
        pass

class LeitorCSV(Arquivo):
    def ler(self) -> List[Dict]:
        """Ler o arquivo CSV"""
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                logger.info(f'Arquivo {self.caminho_arquivo} lido com sucesso')                
                arquivo_csv:List[Dict] = list(csv.DictReader(arquivo))                
                logger.info("Lendo arquivo CSV...")                
                return arquivo_csv
        
        except FileNotFoundError:
            logger.critical(f'Arquivo {self.caminho_arquivo} nao encontrado')
            raise FileNotFoundError(f'Arquivo {self.caminho_arquivo} nao encontrado')
        except Exception as e:
            logger.critical(f'Erro ao ler o arquivo {self.caminho_arquivo}: {e}')
            raise Exception(f'Erro ao ler o arquivo {self.caminho_arquivo}: {e}')
        
class LeitorJSON(Arquivo):
    def ler(self) -> Dict:
        """Ler o arquivo JSON"""
        
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                logger.info(f'Arquivo {self.caminho_arquivo} lido com sucesso')
                dados = json.load(arquivo)                
                logger.info("Lendo arquivo JSON...")
                return dados

        except FileNotFoundError:
            logger.critical(f'Arquivo {self.caminho_arquivo} nao encontrado')
        except json.JSONDecodeError:
            logger.critical(f'Erro ao decodificar o arquivo JSON {self.caminho_arquivo}')
        except Exception as e:
            logger.critical(f'Erro ao ler o arquivo JSON {self.caminho_arquivo}: {e}')

"""
Implemente uma classe abstrata Veiculo com um método abstrato acelerar(). 
Crie subclasses como Carro e Bicicleta e implemente o comportamento do método acelerar()
de forma distinta para cada uma.
"""

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        """Acelera o veiculo"""
        pass

class Carro(Veiculo):
    def acelerar(self):
        """Acelera o carro"""
        logger.info("Acelerando o carro...")
        return "Acelerando o carro..."

class Bicicleta(Veiculo):
    def acelerar(self):
        """Acelera a bicicleta"""
        logger.info("Acelerando a bicicleta...")
        return "Acelerando a bicicleta..."

"""
Crie uma classe abstrata ContaBancaria com os métodos depositar() e sacar(). 
Implemente subclasses como ContaCorrente e ContaPoupanca, 
customizando as regras de cada tipo de conta.
"""

class ContaBancaria(ABC):
    def __init__(self, saldo_inicial:float=0.0):
        self.saldo = saldo_inicial
    @abstractmethod
    def depositar(self):
        """Deposita na conta bancaria"""
        pass

    @abstractmethod
    def sacar(self):
        """Saca da conta bancaria"""
        pass

class ContaCorrente(ContaBancaria):
    def depositar(self, valor:float) -> float:
        
        if not isinstance(valor, (int, float)):
            logger.error(f"O valor {valor} nao eh valido. Valor deve ser um numero.")
            raise ValueError(f"O valor {valor} nao eh valido. Valor deve ser um numero.")
        
        if valor <= 0:
            logger.error(f"O valor {valor} nao eh valido. Valor deve ser maior que zero.")
            raise ValueError(f"O valor {valor} nao eh valido. Valor deve ser maior que zero.")
        
        
        try:
            self.saldo += valor
            logger.info(f"Depositando {valor} na conta corrente. Saldo atual: {self.saldo}")
        
        except Exception as e:
            logger.critical(f"Erro ao depositar {valor} na conta corrente: {e}")
            raise Exception(f"Erro ao depositar {valor} na conta corrente: {e}")

        logger.info('Depósito concluído com sucesso.')

        return self.saldo

    def sacar(self,valor:float) -> float:
        if not isinstance(valor, (int, float)):
            logger.error(f"O valor {valor} não é válido. O valor deve ser um número.")
            raise ValueError(f"O valor {valor} não é válido. O valor deve ser um número.")
        
        if valor <= 0:
            logger.error(f"O valor {valor} não é válido. O valor deve ser maior que zero.")
            raise ValueError(f"O valor {valor} não é válido. O valor deve ser maior que zero.")
        
        if valor > self.saldo:
            logger.error(f"Saldo insuficiente para realizar o saque de {valor}. Saldo disponível: {self.saldo}.")
            raise ValueError(f"Saldo insuficiente para realizar o saque de {valor}. Saldo disponível: {self.saldo}.")
        
        try:
            self.saldo -= valor
            logger.info(f"Sacando {valor} da conta corrente. Saldo atual: {self.saldo}")
        
        except Exception as e:
            logger.critical(f"Erro ao sacar {valor} da conta corrente: {e}")
            raise Exception(f"Erro ao sacar {valor} da conta corrente: {e}")

        logger.info(f"Saque concluído com sucesso. Saldo atualizado: {self.saldo}")
        return self.saldo

class ContaPoupanca(ContaBancaria):
    def depositar(self, valor: float) -> float:
        
        if not isinstance(valor, (int, float)):
            logger.error(f"O valor {valor} não é válido. O valor deve ser um número.")
            raise ValueError(f"O valor {valor} não é válido. O valor deve ser um número.")
        
        if valor <= 0:
            logger.error(f"O valor {valor} não é válido. O valor deve ser maior que zero.")
            raise ValueError(f"O valor {valor} não é válido. O valor deve ser maior que zero.")
        
        try:
            self.saldo += valor
            logger.info(f"Depositando {valor} na conta poupança. Saldo atual: {self.saldo}")
        
        except Exception as e:
            logger.critical(f"Erro ao depositar {valor} na conta poupança: {e}")
            raise Exception(f"Erro ao depositar {valor} na conta poupança: {e}")

        logger.info(f"Depósito concluído com sucesso. Saldo atualizado: {self.saldo}")
        return self.saldo
    
    def sacar(self, valor: float) -> float:
        
        if not isinstance(valor, (int, float)):
            logger.error(f"O valor {valor} não é válido. O valor deve ser um número.")
            raise ValueError(f"O valor {valor} não é válido. O valor deve ser um número.")
        
        if valor <= 0:
            logger.error(f"O valor {valor} não é válido. O valor deve ser maior que zero.")
            raise ValueError(f"O valor {valor} não é válido. O valor deve ser maior que zero.")
        
        if valor > self.saldo:
            logger.error(f"Saldo insuficiente para realizar o saque de {valor}. Saldo disponível: {self.saldo}.")
            raise ValueError(f"Saldo insuficiente para realizar o saque de {valor}. Saldo disponível: {self.saldo}.")
        
        try:
            self.saldo -= valor
            logger.info(f"Sacando {valor} da conta poupança. Saldo atual: {self.saldo}")
        
        except Exception as e:
            logger.critical(f"Erro ao sacar {valor} da conta poupança: {e}")
            raise Exception(f"Erro ao sacar {valor} da conta poupança: {e}")

        logger.info(f"Saque concluído com sucesso. Saldo atualizado: {self.saldo}")
        return self.saldo

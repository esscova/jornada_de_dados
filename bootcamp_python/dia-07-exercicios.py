"""

descrição: 
    - exercicios de fixação
    - dia 07 bootcamp python: Funções

autor: 
    - wellington moreira
    - wsantos08@hotmail.com

versão python: 
    - 3.12.4

"""
from typing import List

# Exercícios

# 1. Calcular Média de Valores em uma Lista
def calcular_media(valores:List[float]) -> float:
    """
    Função para calcular a média de uma lista de valores e retorna a média.
    """
    return sum(valores) / len(valores)

# 2. Filtrar Dados Acima de um Limite
def filtrar_dados_acima_limite(valores:List[float], limite:float) -> List[float]:
    """
    Função para filtrar dados acima de um limite, 
    recebe uma lista de valores e um limite.
    """
    return [x for x in valores if x > limite]

# 3. Contar Valores Únicos em uma Lista
def contar_valores_unicos(valores:List[float]) -> int:
    """
    Função para contar os valores únicos em uma lista, 
    recebe uma lista de valores e retorna a quantidade de valores únicos.
    """
    return len(set(valores))

# 4. Converter Celsius para Fahrenheit em uma Lista
def converter_celsius_para_fahrenheit(valores:List[float]) -> List[float]:
    """
    Função para converter celsius para fahrenheit, 
    recebe uma lista de valores e retorna uma nova lista com os valores convertidos.
    """
    return [(x * 9/5) + 32 for x in valores]

# 5. Calcular Desvio Padrão de uma Lista
def calcular_desvio_padrao(valores:List[float]) -> float:
    """
    Função para calcular o desvio padrão de uma lista de valores, 
    recebe uma lista de valores e retorna o desvio padrão.
    """
    media = sum(valores) / len(valores)
    return (sum((x - media) ** 2 for x in valores) / len(valores)) ** 0.5

# 6. Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(valores:List[float]) -> List[float]:
    """
    Função para encontrar valores ausentes em uma sequência, 
    recebe uma lista de valores e retorna uma nova lista com os valores ausentes.
    """
    return [x for x in range(min(valores), max(valores) + 1) if x not in valores]

# main
def main() -> None:
    # Exercício 1
    valores = [10, 20, 30, 40, 50]
    media = calcular_media(valores)
    print(f"Media: {media}")

    # Exercício 2
    limite = 30
    valores_acima_limite = filtrar_dados_acima_limite(valores, limite)
    print(f"Valores acima do limite: {valores_acima_limite}")

    # Exercício 3
    qt_valores_unicos = contar_valores_unicos(valores)
    print(f"Quantidade de valores únicos: {qt_valores_unicos}")

    # Exercício 4
    valores_fahrenheit = converter_celsius_para_fahrenheit(valores)
    print(f"Valores em Fahrenheit: {valores_fahrenheit}")

    # Exercício 5
    desvio_padrao = calcular_desvio_padrao(valores)
    print(f"Desvio padrão: {desvio_padrao}")

    # Exercício 6
    valores_ausentes = encontrar_valores_ausentes(valores)
    print(f"Valores ausentes: {valores_ausentes}")


if __name__ == "__main__":
    main()
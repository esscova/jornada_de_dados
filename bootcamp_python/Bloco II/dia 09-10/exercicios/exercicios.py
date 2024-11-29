import sys
import os
from loguru import logger
import time
import pandas as pd
"""

1. Log no console
Crie um script que registre mensagens de log nos níveis INFO, WARNING e ERROR diretamente no console.

Objetivo:
Compreender os diferentes níveis de log.
Experimentar os métodos logger.info, logger.warning e logger.error.

"""
def logar_mensagens() -> None:
    logger.info('Informacao')
    logger.warning('Aviso')
    logger.error('Erro')

"""
2. Log em Arquivo
Configure o Loguru para salvar os logs em um arquivo chamado aplicacao.log. Registre três mensagens com diferentes níveis de log.

Objetivo:
Aprender a usar o método logger.add para salvar logs em arquivos.
Familiarizar-se com a criação de arquivos de log.

"""
def salvar_em_arquivo() -> None:
    logger.add('aplicacao.log')
    logger.info('Programa iniciado')
    logger.debug('Debug')
    logger.warning('Aviso fechando o programa')

"""
3. Formatação de Mensagens
Personalize o formato do log para incluir a hora, o nível e a mensagem, com o seguinte modelo:
"{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}".

Objetivo:
Explorar o parâmetro format no método logger.add.
Criar mensagens de log claras e legíveis.

"""
def logs_formatados() -> None:
    logger.remove()
    logger.add(sys.stderr, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
    logger.info('logs formatados')
    logger.debug('Debug')
    logger.warning('Aviso fechando o programa')
    logger.error('Erro')

"""
4. Rotação de Arquivos
Configure o Loguru para rotacionar os arquivos de log quando eles atingirem 1 MB. Teste gerando mensagens de log até que a rotação ocorra.

Objetivo:
Praticar o uso do parâmetro rotation para gerenciar tamanhos de arquivos.
Compreender a rotação automática de arquivos.
"""
def rotacionar_arquivos() -> None:
    log_file:str = 'rotacao.log'

    logger.add(log_file, 
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
               rotation='1 MB')

    try:
        for _ in range(9999):
            if os.path.exists(log_file):
                logger.info("Este é um log gerado dinamicamente enquanto o arquivo não atinge 1 MB.")

    except ValueError as e:
        logger.error(f'Erro ao gerar log dinâmico: {e}')
    except KeyboardInterrupt:
        logger.info('Encerrando o programa...')

"""
5. Capturando Exceções
Use o decorador @logger.catch para registrar automaticamente qualquer exceção gerada por uma função que simula um erro (exemplo: divisão por zero).

Objetivo:
Aprender a capturar e registrar rastreamentos completos de erros.
Familiarizar-se com o decorador @logger.catch.
"""
@logger.catch
def divisao_por_zero() -> None:
    return 1 / 0

"""
6. Medindo Tempo de Execução
Implemente um decorador personalizado para medir o tempo de execução de uma função e registre o tempo no log.

Objetivo:
Criar decoradores personalizados.
Usar o Loguru para registrar informações dinâmicas, como tempos de execução.
"""
def medir_tempo(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f'Execução de {func.__name__} demorou {execution_time:.2f} segundos')
        return result
    return wrapper

@medir_tempo
def executar_funcao() -> str:
    time.sleep(3)
    return 'Função executada com sucesso!'

"""
7. Entrada e Saída de Funções
Implemente um decorador que registre:

Os argumentos de entrada de uma função.
O resultado de saída.
Teste com uma função que soma dois números.

Objetivo:
Criar logs úteis para depuração de funções.
Registrar dados dinâmicos nos logs.

"""
def registrar_entrada_saida(func):
    def wrapper(*args, **kwargs):
        logger.info(f'Entrada: {args}, {kwargs}')
        result = func(*args, **kwargs)
        logger.info(f'Saída: {result}')
        return result
    return wrapper

@registrar_entrada_saida
def soma(a, b) -> int:
    return a + b

"""
8. Integração com pandas
Crie um pipeline simples com pandas que:

[X] Leia um arquivo CSV fictício. 
[X] Limpe os dados (ex: remova valores ausentes).
[X] Renomeie colunas. 
[X] Registre cada etapa do pipeline com mensagens de log, incluindo o número de linhas e colunas antes e depois de cada transformação.

Objetivo:
Usar logs para monitorar o progresso de pipelines de dados.
Integrar Loguru em fluxos de trabalho de análise.
"""
import pandas as pd
from loguru import logger

def limpar_dados(arquivo_csv: str) -> pd.DataFrame | None:

    df = pd.read_csv(arquivo_csv, sep=';', encoding='utf-8')

    logger.add('pipeline.log',
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
               rotation='1 MB')
    
    if df.empty:
        logger.error('Arquivo CSV vazio')
        return None

    logger.info('Iniciando pipeline de dados...')
    logger.info(f'Arquivo CSV carregado com {df.shape[0]} linhas e {df.shape[1]} colunas')

    try: 
        logger.info('Verificando valores ausentes...')
        
        if not df.isna().any().any():  
            logger.info('Nenhum valor ausente encontrado.')
        else:
            logger.warning(f'Valores ausentes encontrados: {df.isnull().sum().to_dict()}')
            logger.info('Removendo valores ausentes...')
            df.dropna(inplace=True)
            logger.info(f'Valores ausentes removidos. csv atual com {df.shape[0]} linhas e {df.shape[1]} colunas')

        logger.info('Renomeando colunas...')
        df.rename(columns={'coluna1': 'nova_coluna1', 'coluna2': 'nova_coluna2'}, inplace=True)
        logger.info(f'Colunas renomeadas. csv atual com {df.shape[0]} linhas e {df.shape[1]} colunas')

        logger.info('Pipeline de dados concluído.')
        print(df.head())
        return df

    except Exception as e:
        logger.error(f'Erro na pipeline de dados: {e}')
        return None

"""
9. Criando um decorador
Crie um decorador chamado minha_mensagem que imprime "Iniciando função..." antes de executar uma função e "Função concluída!" depois. Aplique este decorador a uma função chamada saudar, que recebe um nome como argumento e imprime "Olá, [nome]!".

Objetivo:
Entender a estrutura básica de um decorador.
Familiarizar-se com o conceito de wrapper.
"""
def minha_mensagem(func):
    def wrapper(*args, **kwargs):
        print('Iniciando função...')
        result = func(*args, **kwargs)
        print('Função concluida!')
        return result
    return wrapper

@minha_mensagem
def say_my_name(name) -> str:
    print( f'Olá, {name}!' )

"""
10. Decorador com Argumentos Dinâmicos
Crie um decorador chamado log_entrada_saida que registra os argumentos de entrada e o valor de retorno de uma função. 
Aplique este decorador a uma função chamada soma, que recebe dois números e retorna sua soma.

Objetivo:
Aprender a manipular *args e **kwargs no wrapper.
Entender como registrar informações antes e depois da execução da função.
"""
def log_entrada_saida(func):
    def wrapper(*args, **kwargs):
        logger.info(f'Entrando na função: "{func.__name__}"')
        logger.info(f'Entrada: {args}, {kwargs}')
        result = func(*args, **kwargs)
        logger.debug(f'Saida: {result}')
        logger.info(f'Saindo da função: "{func.__name__}"')
        return result
    return wrapper

@log_entrada_saida
def soma_outra_vez(a, b) -> int:
    return a + b

"""
11. Controle de Acesso
Crie um decorador chamado verificar_permissao que aceita como argumento um nome de usuário permitido. 
O decorador deve permitir a execução da função apenas se o usuário passado como argumento for o mesmo do permitido; 
caso contrário, deve levantar uma exceção PermissionError. Aplique o decorador a uma função chamada acessar_dados, que imprime "Acesso concedido".

Objetivo:
Trabalhar com decoradores parametrizados.
Implementar lógica condicional dentro do wrapper.
"""
def verficar_permissao(usuario_permitido: str):
    def decorator(func):
        def wrapper(user:str, *args, **kwargs):
            if user != usuario_permitido:
                logger.error(f'Acesso negado para {user}')
            else:
                logger.info(f'Acesso concedido para {user}')
                return func(user, *args, **kwargs)

        return wrapper
    
    return decorator

def main() -> None:
    logar_mensagens()
    salvar_em_arquivo()
    logs_formatados()
    rotacionar_arquivos()
    divisao_por_zero()
    executar_funcao()
    soma(1, b=2)
    limpar_dados('exemplo.csv')
    say_my_name('Heisenberg')
    soma_outra_vez(22, 61)
    
    @verficar_permissao('escova')
    def acessar_dados(usuario:str):
        logger.info('Dados sensíveis acessados.')
    
    acessar_dados('admin')
    acessar_dados('escova')

if __name__ == '__main__':
    main()
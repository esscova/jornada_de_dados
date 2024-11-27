# Jornada de dados - Bootcamp Python: Parte II
## Avançando com estruturas de dados e funções em Python

Este repositório foi organizado conforme os meus estudos no treinamento em Python para engenheiros de dados da [Jornada de dados](https://suajornadadedados.com.br/). É recomendado àqueles que já possuem uma base em Python e desejam aprofundar seus conhecimentos em estruturas de dados avançadas e em como usar funções de maneira mais eficiente. Além disso, vamos explorar ferramentas de formatação de código, como `flake8`, `black`, `blue`, e `pre-commit`, além de tópicos avançados sobre funções, como decorators e lambdas. Esses conceitos são cruciais para escrever código mais limpo, modular e eficiente.

## Índice

1. [Formatação de Código com Flake8, Black, Blue e Pre-Commit](#formatação-de-código-com-flake8-black-blue-e-pre-commit)
2. [Funções em Python: Nível Intermediário](#funções-em-python-nível-intermediário)
3. [Funções Decorator](#funções-decorator)
4. [Funções Lambda](#funções-lambda)
5. [Logs com Loguru e Funções com Logs para Engenharia de Dados](#logs-com-loguru-e-funções-com-logs-para-engenharia-de-dados)

---

## Formatação de Código com Flake8, Black, Blue e Pre-Commit

Em projetos de engenharia de dados, especialmente em ambientes colaborativos, é essencial manter um código legível e consistente. A formatação automática de código ajuda a evitar erros comuns e melhora a manutenção do código. Ferramentas como `flake8`, `black`, `blue`, e `pre-commit` são amplamente utilizadas para garantir que seu código siga padrões de estilo e boas práticas de Python.

### Flake8

O `flake8` é uma ferramenta de linting que verifica o código para erros de estilo, erros de sintaxe e problemas de qualidade. Ela ajuda a garantir que seu código siga a PEP 8, o guia oficial de estilo de código do Python.

### Exemplo de uso do Flake8:
```bash
# Instalando o flake8
pip install flake8

# Executando o flake8 no código
flake8 nome_do_arquivo.py
```

### Black

O `black` é um formatador de código que formata automaticamente seu código de acordo com as convenções de estilo. O `black` tem como principal objetivo garantir que todos os códigos sigam um único padrão, evitando discussões sobre estilo entre desenvolvedores.

### Exemplo de uso do Black:
```bash
# Instalando o black
pip install black

# Formatando o código
black nome_do_arquivo.py
```

### Blue

O `blue` é uma alternativa ao `black`, que também formata automaticamente o código, mas com um foco maior em manter a legibilidade, especialmente em casos de linhas longas.

### Exemplo de uso do Blue:
```bash
# Instalando o blue
pip install blue

# Formatando o código
blue nome_do_arquivo.py
```

### Pre-Commit

O `pre-commit` é uma ferramenta que permite configurar ganchos (hooks) para executar ações antes de confirmar mudanças no código (commit). Isso é útil para garantir que seu código esteja formatado corretamente antes de ser enviado para o repositório.

### Exemplo de configuração do pre-commit:
```bash
# Instalando o pre-commit
pip install pre-commit

# Criando o arquivo de configuração .pre-commit-config.yaml
pre-commit install

# Rodando os hooks do pre-commit
pre-commit run --all-files
```

Integrar essas ferramentas no seu fluxo de trabalho melhora a qualidade do código e evita problemas relacionados à formatação ou estilo.

Agora, vamos seguir para o uso mais avançado de funções em Python, que é uma habilidade essencial para escrever código modular e reutilizável.

---

## Funções em Python: Nível Intermediário

Embora você já tenha aprendido o básico sobre funções em Python, é importante entender como utilizar funções de maneira mais avançada. Funções intermediárias permitem que você escreva código mais conciso e reutilizável, além de melhorar a performance e organização do seu programa.

### Argumentos Variáveis

Você pode criar funções que aceitam um número variável de argumentos. Isso é útil quando você não sabe exatamente quantos argumentos serão passados para a função.

### Exemplo de função com argumentos variáveis:
```python
# Função que aceita um número variável de argumentos
def soma(*args):
    return sum(args)

# Chamando a função
print(soma(1, 2, 3))  # Saída: 6
```

Esse tipo de função é útil em situações como quando você precisa somar um conjunto de números que pode variar de uma execução para outra.

### Funções com Argumentos Nomeados

Você também pode definir funções que aceitam parâmetros nomeados. Esses parâmetros tornam seu código mais legível e permitem que você passe argumentos em qualquer ordem.

### Exemplo de função com argumentos nomeados:
```python
# Função com parâmetros nomeados
def exibir_info(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

# Chamando a função
exibir_info(idade=30, nome="João")
```

Passar argumentos nomeados é uma maneira excelente de melhorar a clareza do código, especialmente quando se trabalha com funções que possuem muitos parâmetros.

---

## Funções Decorator

Os **decorators** em Python são uma maneira de modificar o comportamento de uma função sem alterá-la diretamente. Em engenharia de dados, decorators são úteis para tarefas como validação de dados, cálculos de performance e logging.

### Exemplo de função decorator:
```python
# Função decorator para medir o tempo de execução
import time

def cronometro(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo de execução: {end_time - start_time} segundos")
        return result
    return wrapper

# Usando o decorator
@cronometro
def processar_dados():
    # Simulando um processamento de dados
    time.sleep(2)
    print("Dados processados!")

processar_dados()
```

No exemplo acima, a função `cronometro` serve como um decorator que mede o tempo de execução de qualquer função à qual ela seja aplicada. Decorators são poderosos para adicionar funcionalidades como logs ou métricas sem alterar o código original da função.

Agora, que entendemos como usar decorators, vamos aprender sobre **funções lambda**, que são funções anônimas e podem ser muito úteis para tarefas rápidas e concisas.

---

## Funções Lambda

As **funções lambda** são funções anônimas que podem ser criadas de forma compacta. Elas são especialmente úteis quando você precisa de uma função simples para ser usada temporariamente, sem a necessidade de definir uma função completa com `def`.

### Exemplo de função lambda:
```python
# Função lambda para somar dois números
soma = lambda a, b: a + b
print(soma(3, 5))  # Saída: 8
```

Embora as funções `lambda` sejam compactas e úteis em certos contextos, elas não devem ser usadas para lógica complexa. Elas são ideais para funções simples e funções passadas como argumentos para outras funções, como em `map()`, `filter()` e `sorted()`.

### Exemplo de uso de `lambda` com `sorted()`:
```python
# Ordenando uma lista de tuplas com base no segundo item usando lambda
dados = [(1, "João"), (2, "Maria"), (3, "Pedro")]
dados_ordenados = sorted(dados, key=lambda x: x[1])
print(dados_ordenados)
```

Em engenharia de dados, as funções `lambda` são úteis para transformar ou filtrar dados rapidamente, como ao processar listas ou conjuntos de dados com `map()` ou `filter()`.

---

## Logs com Loguru e Funções com Logs para Engenharia de Dados

Em projetos de engenharia de dados, a monitoração e o rastreamento de processos são essenciais para identificar e corrigir problemas rapidamente. O uso de logs facilita a depuração e o monitoramento da performance do código.

### Loguru

O `loguru` é uma biblioteca de logging fácil de usar e que oferece recursos avançados, como rotação automática de arquivos de log, controle de nível de logs e configuração simplificada.

### Exemplo básico de uso do Loguru:
```python
from loguru import logger

# Configurando o logger
logger.add("logfile.log", rotation="500 MB")

# Registrando um log
logger.info("Início do processamento de dados")

# Registrando um erro
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Erro ao tentar dividir por zero")
```

O `loguru` facilita a configuração de logs e garante que você tenha informações detalhadas sobre o que está acontecendo em sua aplicação, o que é crucial em pipelines de dados.

### Funções com Logs

Ao trabalhar com grandes volumes de dados ou pipelines complexos, é fundamental registrar informações sobre o processo. Usando logs, você pode monitorar o tempo de execução de funções, identificar erros e avaliar o desempenho.

### Exemplo de função com logs:
```python
from loguru import logger

def processar_dados(dados):
    logger.info("Iniciando o processamento de dados")
    try:
        # Simulando um processamento de dados
        result = [dado * 2 for dado in dados]
        logger.info(f"Processamento concluído. Resultados: {result}")
    except Exception as e:
        logger.error(f"Erro ao process

ar os dados: {e}")
    return result

# Chamando a função
processar_dados([1, 2, 3])
```

O uso de logs facilita o diagnóstico de problemas e ajuda a rastrear a evolução do trabalho, especialmente em ambientes de produção.

---

## Considerações finais

Neste repositório, exploramos técnicas avançadas de Python que são essenciais para engenheiros de dados, incluindo a formatação de código com ferramentas como `flake8`, `black`, e `blue`, além de funções intermediárias, decorators, lambdas e logs. Esses conceitos são fundamentais para manter seu código limpo, eficiente e fácil de depurar, além de permitir que você escreva código mais modular e reutilizável.

Agora, você está pronto para aplicar essas habilidades no seu dia a dia de engenharia de dados, seja em manipulação de grandes volumes de dados, automação de processos ou rastreamento de erros. Python oferece uma ampla gama de ferramentas e técnicas para ajudar a enfrentar os desafios do mundo real, e dominar essas habilidades certamente fará de você um desenvolvedor mais eficiente e eficaz.
### **Guia Completo do Loguru: Da Instalação à Aplicação Prática**

Seja você um engenheiro de dados, um cientista de dados ou um desenvolvedor lidando com sistemas complexos, o gerenciamento eficiente de logs é fundamental para garantir que tudo funcione como planejado. A biblioteca **Loguru** transforma a maneira de lidar com logs, fornecendo simplicidade, flexibilidade e poder sem as complicações do módulo padrão `logging`. 

Este guia irá acompanhá-lo passo a passo desde a instalação até casos práticos em sua aplicação.

<p align='center'><img src='https://raw.githubusercontent.com/Delgan/loguru/master/docs/_static/img/logo.png'></p>

**Github**: [https://github.com/Delgan/loguru](https://github.com/Delgan/loguru)

**Documentação**: [https://loguru.readthedocs.io/en/stable/](https://loguru.readthedocs.io/en/stable/)

---

## **1. Introdução ao Loguru**

O Loguru foi criado para tornar o trabalho com logs mais intuitivo e eficiente. Ele oferece:
- **Configuração simplificada**: Você pode começar com apenas uma linha de código.
- **Mensagens ricas e personalizáveis**: Informações detalhadas como horários, níveis de log, arquivos e linhas.
- **Rotação e retenção de arquivos**: Ideal para monitoramento contínuo em produção.
- **Captura de exceções**: Incluindo rastreamento completo da pilha de erros.
- **Integração com bibliotecas existentes**: Compatível com `pandas`, `airflow` e muito mais.

---

## **2. Instalação**

Antes de começar, instale o Loguru em seu ambiente Python:

```bash
pip install loguru
```

Com a biblioteca instalada, você já está pronto para criar seus primeiros logs.

---

## **3. Uso Básico**

O Loguru permite registrar mensagens de log de forma extremamente simples:

```python
from loguru import logger

logger.info("Esta é uma mensagem de log informativa!")
logger.warning("Cuidado! Algo pode estar errado.")
logger.error("Ocorreu um erro inesperado.")
```

**Saída no console:**
```
2024-11-22 14:30:12.123 | INFO     | __main__:<module>:2 - Esta é uma mensagem de log informativa!
2024-11-22 14:30:12.124 | WARNING  | __main__:<module>:3 - Cuidado! Algo pode estar errado.
2024-11-22 14:30:12.125 | ERROR    | __main__:<module>:4 - Ocorreu um erro inesperado.
```

Próximo passo? Configurar os logs para armazenar mensagens em arquivos.

---

## **4. Salvando Logs em Arquivos**

Para aplicações reais, registrar logs apenas no console não é suficiente. Com o Loguru, você pode salvar logs em arquivos e configurar comportamentos avançados como **rotação** e **retenção**:

```python
logger.add("logs/app.log", rotation="500 MB", retention="10 days", compression="zip")

logger.info("Mensagem será salva no arquivo de log.")
```

**O que acontece?**
- Um novo arquivo será criado quando o tamanho exceder 500 MB.
- Logs mais antigos que 10 dias serão removidos automaticamente.
- Arquivos antigos são compactados para economizar espaço.

Essa configuração é ideal para sistemas que geram grandes volumes de logs, como pipelines de dados.

---

## **5. Aplicação Prática na Engenharia e Ciência de Dados**

### **5.1 Monitoramento de Treino de Modelos**
Cientistas de dados frequentemente enfrentam desafios ao monitorar o treinamento de modelos que podem levar horas ou dias. O Loguru facilita o rastreamento desses processos:

```python
from loguru import logger
import time

logger.add("logs/model_training.log", format="{time} | {level} | {message}", level="INFO")

# Simulação de treino de modelo
for epoch in range(1, 6):
    try:
        logger.info(f"Treinando o modelo - Época {epoch}")
        if epoch == 3:  # Simular erro na terceira época
            raise ValueError("Erro no modelo durante a época 3!")
        time.sleep(1)  # Simulação do tempo de treino
    except Exception as e:
        logger.error(f"Erro detectado: {e}")
```

**Benefícios:**
- Cada iteração do treinamento é registrada, com detalhes claros sobre erros.
- Logs ficam disponíveis para análise posterior, útil para debugging e auditoria.

---

### **5.2 Logs em Pipelines de ETL**

Engenheiros de dados frequentemente lidam com pipelines que processam grandes volumes de informações. Aqui está como o Loguru pode ajudar a manter os logs sob controle:

```python
from loguru import logger

logger.add(
    "logs/data_pipeline.log",
    rotation="1 day",
    retention="7 days",
    compression="zip"
)

# Simulando um pipeline de ETL
for i in range(10):
    logger.info(f"Processando lote {i + 1}")
    if i == 5:  # Simular erro no meio do pipeline
        logger.error("Falha ao processar lote 6: Falta de memória.")
```

**Como funciona?**
- Logs são rotacionados diariamente.
- Logs antigos são mantidos por no máximo 7 dias.
- Compressão reduz o impacto no armazenamento.

Esse padrão garante que os logs de seus pipelines sejam gerenciados automaticamente, sem necessidade de manutenção manual.

---

## **6. Captura de Exceções**

Erros inesperados podem ser capturados de forma elegante com o Loguru:

### **Decorando Funções**
Com o método `@catch`, você pode capturar exceções automaticamente:

```python
from loguru import logger

@logger.catch
def dividir(a, b):
    return a / b

dividir(10, 0)
```

**Saída:**
```
2024-11-22 14:30:00.123 | ERROR    | __main__:dividir:3 - ZeroDivisionError: division by zero
```

### **Capturando Erros em Blocos Try/Except**
Se preferir, pode capturar manualmente exceções e registrar detalhes:

```python
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Erro ao dividir.")
```

Esses métodos são ideais para rastrear problemas críticos em sistemas de produção.

---

## **7. Integração com Outras Bibliotecas**

Se você usa bibliotecas como `pandas` ou `airflow`, pode redirecionar os logs para o Loguru:

```python
import logging
from loguru import logger
import pandas as pd

class InterceptHandler(logging.Handler):
    def emit(self, record):
        loguru_level = logger.level(record.levelname).name
        logger.log(loguru_level, record.getMessage())

logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)

try:
    df = pd.DataFrame({"coluna": [1, 2, "erro"]})
    df["coluna"] = df["coluna"].astype(int)  # Gera erro
except Exception as e:
    logger.exception("Erro ao converter coluna para inteiro.")
```

**Por que usar?**
- Todos os logs do `pandas` ou bibliotecas similares são centralizados no Loguru.
- Ideal para fluxos de trabalho complexos em ETL ou processamento de dados.

---

## **8. Configurações Avançadas**

Para projetos maiores, você pode usar arquivos de configuração em JSON ou YAML. Exemplo em JSON:

**Arquivo `config.json`:**
```json
{
    "handlers": [
        {
            "sink": "logs/debug.log",
            "level": "DEBUG",
            "format": "{time} {level} {message}",
            "rotation": "1 week"
        }
    ]
}
```

**Carregar Configuração no Código:**
```python
from loguru import logger
import json

with open("config.json", "r") as file:
    config = json.load(file)

logger.configure(**config)
```

---

## **9. Considerações finais**

O Loguru oferece um conjunto de recursos poderosos e fáceis de usar que podem transformar a maneira como você gerencia logs em projetos de engenharia ou ciência de dados. Desde monitorar o progresso de modelos até rastrear fluxos de dados em pipelines complexos, ele é uma solução indispensável para quem busca simplicidade e eficiência.

Implemente o Loguru em um de seus projetos e experimente a diferença na prática. 
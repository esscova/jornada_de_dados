# **Decoradores em Python com Loguru: Monitoramento e Registro Inteligente**

Decoradores são uma das ferramentas mais elegantes e poderosas em Python, permitindo que você adicione funcionalidades extras às suas funções sem alterar diretamente seu código. Quando combinados com o **Loguru**, um dos frameworks mais populares para registro de logs em Python, eles se tornam uma solução prática e sofisticada para monitorar execuções, registrar erros e medir desempenho.

Neste guia, você verá exemplos reais e aplicáveis ao dia a dia de analistas, cientistas e engenheiros de dados. Desde capturar erros automaticamente até rastrear transformações em pipelines, descubra como **decoradores com Loguru** podem simplificar e melhorar a qualidade do seu trabalho.

---

## **O que são Decoradores e como Funcionam?**

Antes de mergulhar nos exemplos, vamos revisitar rapidamente o conceito de decoradores. Um decorador é uma função que "envolve" outra função, adicionando ou alterando seu comportamento. Para fazer isso, ele utiliza o **wrapper**, uma camada onde você pode adicionar lógica extra.

Um aspecto fundamental no wrapper é o uso de `*args` e `**kwargs`. Esses parâmetros permitem que o decorador aceite qualquer combinação de argumentos da função original, garantindo sua flexibilidade. Aqui está um exemplo simples para refrescar sua memória:

```python
def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da função.")
        resultado = func(*args, **kwargs)
        print("Depois da função.")
        return resultado
    return wrapper

@meu_decorador
def diga_ola(nome):
    print(f"Olá, {nome}!")

diga_ola("Maria")
```

Agora que entendemos o básico, vamos explorar como Loguru eleva a utilidade dos decoradores para o próximo nível.

---

## **Exemplo 1: Registro Automático de Exceções**
Erros são inevitáveis, mas perder rastreamentos críticos pode tornar a depuração uma tarefa assustadora. O Loguru simplifica isso com o decorador `@logger.catch`, que captura e registra automaticamente quaisquer exceções levantadas dentro de uma função.

### **Código:**
```python
from loguru import logger

@logger.catch
def dividir(a, b):
    return a / b

# Exemplo de chamada
dividir(10, 0)
```

### **Saída do Log:**
```
2024-11-22 14:30:00.123 | ERROR    | __main__:dividir:3 - ZeroDivisionError: division by zero
```

### **Por que usar?**
- Captura automaticamente todos os erros dentro da função.
- Útil para funções críticas, como cálculos matemáticos ou operações de banco de dados.

**Próxima aplicação:** Além de capturar erros, que tal medir o tempo que uma função leva para executar? Vamos ver como fazer isso.

---

## **Exemplo 2: Medindo Tempo de Execução**
Para otimizar processos pesados, como treinamentos de modelos ou ETLs, medir o desempenho das funções é essencial. Decoradores personalizados combinados com Loguru permitem monitorar o tempo de execução e registrar os resultados automaticamente.

### **Código:**
```python
from loguru import logger
import time

def log_execucao(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        duracao = time.time() - inicio
        logger.info(f"Função '{func.__name__}' executada em {duracao:.2f} segundos")
        return resultado
    return wrapper

@log_execucao
def tarefa_demorada():
    time.sleep(2)  # Simula uma tarefa demorada

# Exemplo de chamada
tarefa_demorada()
```

### **Saída do Log:**
```
2024-11-22 14:32:15.456 | INFO     | __main__:wrapper:7 - Função 'tarefa_demorada' executada em 2.00 segundos
```

### **Por que usar?**
- Permite identificar gargalos de desempenho.
- Ideal para funções pesadas ou pipelines complexos.

**Conexão com o próximo exemplo:** Saber o desempenho é importante, mas rastrear entradas e saídas também é essencial. Vamos abordar isso agora.

---

## **Exemplo 3: Registro de Entradas e Saídas**
Registrar automaticamente os argumentos recebidos e os resultados de funções facilita a depuração, especialmente em sistemas complexos com muitas variáveis dinâmicas.

### **Código:**
```python
from loguru import logger

def log_entrada_saida(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Executando '{func.__name__}' com argumentos: {args}, {kwargs}")
        resultado = func(*args, **kwargs)
        logger.info(f"Resultado de '{func.__name__}': {resultado}")
        return resultado
    return wrapper

@log_entrada_saida
def soma(a, b):
    return a + b

# Exemplo de chamada
soma(5, 10)
```

### **Saída do Log:**
```
2024-11-22 14:34:01.789 | INFO     | __main__:wrapper:5 - Executando 'soma' com argumentos: (5, 10), {}
2024-11-22 14:34:01.790 | INFO     | __main__:wrapper:7 - Resultado de 'soma': 15
```

### **Por que usar?**
- Garante visibilidade total do fluxo de dados.
- Útil para funções com múltiplas etapas e parâmetros dinâmicos.

**Próxima etapa:** Como aplicar isso em pipelines de transformação de dados? Vamos descobrir.

---

## **Exemplo 4: Monitorando Transformações em Pipelines**
Em pipelines de dados, monitorar cada etapa do processo é crucial para auditorias e depuração. Decoradores simplificam essa tarefa, rastreando cada transformação automaticamente.

### **Código:**
```python
from loguru import logger
import pandas as pd

def log_transformacao(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Iniciando transformação: {func.__name__}")
        resultado = func(*args, **kwargs)
        logger.info(f"Transformação '{func.__name__}' concluída")
        return resultado
    return wrapper

@log_transformacao
def limpar_dados(df):
    return df.dropna()

@log_transformacao
def renomear_colunas(df, colunas):
    return df.rename(columns=colunas)

# Exemplo de chamada
dados = pd.DataFrame({"A": [1, 2, None], "B": [4, None, 6]})
dados = limpar_dados(dados)
dados = renomear_colunas(dados, {"A": "Coluna1", "B": "Coluna2"})
```

### **Saída do Log:**
```
2024-11-22 14:35:12.345 | INFO     | __main__:wrapper:5 - Iniciando transformação: limpar_dados
2024-11-22 14:35:12.346 | INFO     | __main__:wrapper:7 - Transformação 'limpar_dados' concluída
2024-11-22 14:35:12.347 | INFO     | __main__:wrapper:5 - Iniciando transformação: renomear_colunas
2024-11-22 14:35:12.348 | INFO     | __main__:wrapper:7 - Transformação 'renomear_colunas' concluída
```

### **Por que usar?**
- Rastreia claramente o progresso de transformações.
- Facilita depuração e auditoria de pipelines.

**Próxima ideia:** E se uma função falhar temporariamente? Vamos explorar como criar tentativas automáticas.

---

## **Exemplo 5: Repetição Automática com Log**
Quando funções podem falhar intermitentemente (como conexões de API ou banco de dados), um decorador pode implementar tentativas automáticas, registrando cada tentativa e o resultado.

### **Código:**
```python
from loguru import logger
import time
import random

def log_retentativas(tentativas=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for tentativa in range(1, tentativas + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Tentativa {tentativa} falhou: {e}")
                    time.sleep(1)
            logger.error(f"Todas as {tentativas} tentativas falharam para '{func.__name__}'")
        return wrapper
    return decorator

@log_retentativas(tentativas=3)
def conectar_api():
    if random.choice([True, False]):
        raise ConnectionError("Falha na conexão!")
    return "Conexão bem-sucedida!"

# Exemplo de chamada
conectar_api()
```

### **Saída do Log:**
```
2024-11-22 14:36:10.123 | WARNING  | __main__:wrapper:7 - Tentativa 1 falhou: Falha na conexão!
2024-11-22 14:36:11.124 | WARNING  | __main__:wrapper:7 - Tentativa 2 falhou: Falha na conexão!
2024-11-22 14:36:12.125 | ERROR    | __main__:wrapper:10 - Todas as 3 tentativas falharam para 'conectar_api'
```

---

## **A combinação perfeita **
Os exemplos apresentados mostram como **decoradores combinados com Loguru** podem transformar seu código em uma ferramenta poderosa para monitorar, registrar e otimizar processos. Ao implementar esses conceitos, você melhora não só a eficiência, mas também a confiabilidade e a transparência do seu sistema. Experimente personalizar esses exemplos e veja o impacto direto no seu dia a dia!
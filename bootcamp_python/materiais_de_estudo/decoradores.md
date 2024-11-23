# **Decoradores em Python**
## Aprenda a Automatizar e Elevar Suas Funções

Imagine poder adicionar às suas funções novas funcionalidades como: registrar automaticamente o que elas fazem, medir sua eficiência ou até controlar quem pode executá-las – tudo isso sem modificar o código principal. No mundo dos dados, onde eficiência e organização são essenciais, os **decoradores em Python** oferecem exatamente essa mágica. Se você é analista, cientista ou engenheiro de dados, dominar decoradores pode revolucionar seu trabalho.

---

## **Introdução: Por que Decoradores Importam?**
No seu dia a dia, é comum encontrar situações em que você precisa reutilizar comportamentos, como registrar logs de execução, medir tempos de processamento ou validar entradas. Fazer isso manualmente em todas as funções não apenas gera redundância, mas torna o código menos legível. Decoradores resolvem esse problema de forma elegante, permitindo que você adicione funcionalidades extras de maneira reutilizável e organizada.

---

## **Entendendo o Conceito: O Que São Decoradores?**
Decoradores são funções que “envolvem” outras funções, adicionando ou alterando seu comportamento sem mexer no código original. Em Python, são aplicados com o símbolo `@`, seguido do nome do decorador, diretamente acima da função que você deseja modificar.

Por trás dos bastidores, os decoradores funcionam utilizando uma estrutura chamada **wrapper**. O wrapper é onde você insere a lógica adicional que será executada antes ou depois da função decorada. Ele utiliza `*args` e `**kwargs`, que são formas de capturar argumentos posicionais e nomeados, garantindo que qualquer função possa ser decorada, independentemente de sua assinatura.

Vamos entender isso com um exemplo básico:
```python
def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da execução.")
        resultado = func(*args, **kwargs)
        print("Depois da execução.")
        return resultado
    return wrapper

@meu_decorador
def diga_ola(nome):
    print(f"Olá, {nome}!")

diga_ola("Maria")
```

### **Destrinchando o Código:**
1. **`func`**: É a função original que será decorada.
2. **`wrapper`**: É a camada extra ao redor da função decorada. Aqui você pode adicionar lógica personalizada.
3. **`*args` e `**kwargs`**: Garantem que o decorador seja genérico, aceitando qualquer tipo de argumento.
4. **`return wrapper`**: Retorna o wrapper para substituir a função original.

---

### **Aplicações no Dia a Dia de Profissionais de Dados**

Agora que entendemos a teoria, vamos ver como decoradores podem ser aplicados em cenários práticos e impactantes no mundo dos dados.

---

### **1. Registro de Funções para Auditoria**
No trabalho com dados, especialmente ao executar transformações ou consultar bancos de dados, é importante registrar automaticamente o histórico de execução. Decoradores facilitam isso, gerando logs detalhados sem esforço manual.

#### **Exemplo Prático:**
```python
import datetime

def log_execucao(func):
    def wrapper(*args, **kwargs):
        agora = datetime.datetime.now()
        print(f"[{agora}] Executando {func.__name__} com args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"[{agora}] Finalizado {func.__name__}")
        return resultado
    return wrapper

@log_execucao
def consulta_dados(query):
    print(f"Executando consulta: {query}")
    # Simula uma consulta ao banco
    return "Resultados"

# Uso
consulta_dados("SELECT * FROM vendas WHERE ano = 2023")
```

#### **Por que é útil?**
- Ajuda a rastrear o que foi executado, quando e como.
- Facilita auditorias e análises de erros.

**Próxima parada:** E se precisarmos medir o tempo que essas funções levam para executar? Vamos explorar isso a seguir.

---

### **2. Temporização de Processos**
Imagine treinar um modelo ou processar um conjunto de dados massivo. Saber quanto tempo essas operações levam pode ajudar a identificar gargalos e otimizar o pipeline. Um decorador pode automatizar essa medição de tempo.

#### **Exemplo Prático:**
```python
import time

def temporizador(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução de {func.__name__}: {fim - inicio:.2f} segundos")
        return resultado
    return wrapper

@temporizador
def treinar_modelo(dados):
    print("Treinando modelo...")
    time.sleep(3)  # Simula um tempo de execução longo
    print("Modelo treinado!")
    return "Modelo Finalizado"

# Uso
treinar_modelo("dados.csv")
```

#### **Por que é útil?**
- Automatiza a análise de desempenho.
- Ajuda a identificar funções que precisam de otimização.

**A seguir:** Além de medir o tempo, como garantir que apenas pessoas autorizadas ou parâmetros válidos sejam aceitos? Vamos explorar decoradores para validação.

---

### **3. Controle de Acesso e Validação**
Engenheiros de dados frequentemente precisam proteger pipelines críticos ou validar parâmetros recebidos. Decoradores permitem criar um controle centralizado e reutilizável para esses cenários.

#### **Exemplo Prático:**
```python
def valida_usuario(usuario_esperado):
    def decorador(func):
        def wrapper(usuario, *args, **kwargs):
            if usuario != usuario_esperado:
                raise PermissionError("Acesso negado.")
            print(f"Acesso concedido para {usuario}.")
            return func(usuario, *args, **kwargs)
        return wrapper
    return decorador

@valida_usuario("admin")
def executar_pipeline(usuario, pipeline):
    print(f"Executando pipeline {pipeline}...")
    return "Pipeline finalizado!"

# Uso
try:
    executar_pipeline("admin", "pipeline_ETL")
    executar_pipeline("guest", "pipeline_ETL")
except PermissionError as e:
    print(e)
```

#### **Por que é útil?**
- Evita acessos não autorizados.
- Reduz erros ao validar condições críticas automaticamente.

**E mais:** Decoradores não só ajudam em tarefas repetitivas, mas também são úteis na criação de padrões reutilizáveis. Vamos conectar tudo isso na conclusão.

---

## **Decoradores, são seus aliados**
Decoradores são mais do que uma funcionalidade conveniente – eles são uma forma de estruturar seu código de maneira eficiente e profissional. Desde registrar logs até controlar acessos e validar entradas, essas ferramentas tornam seu código mais limpo, robusto e escalável.

Ao dominar decoradores, você não só melhora sua produtividade, como também demonstra maturidade como desenvolvedor Python. Então, experimente os exemplos e pense: o que mais você poderia simplificar ou automatizar com decoradores? 🚀
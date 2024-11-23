# Bootcamp Python: Funções

## Logging
Logging é o processo de gravar mensagens que documentam os eventos que ocorrem durante a execução de um software. Essas mensagens podem indicar progresso da execução, falhas, erros, ou outras informações úteis. O logging é crucial para desenvolvimento e manutenção de software, pois permite aos desenvolvedores e administradores de sistema entender o que o aplicativo está fazendo, diagnosticar problemas e monitorar o desempenho em produção.

<p align = 'center'><img src='https://files.realpython.com/media/Python-Logging-A-Stroll-Through-The-Source-Code_Watermarked.efa1d31c4fe4.jpg' width=500></p>

Para este processo usaremos o [loguru](loguru.readthedocs.io/) uma biblioteca de logging para Python que visa trazer uma experiência de uso mais simples e poderosa do que o módulo de logging padrão do Python. Com uma API simples, Loguru oferece várias funcionalidades úteis, como rotação de arquivos, serialização JSON, envio de mensagens para múltiplos destinos, e muito mais, tudo isso sem a necessidade de configuração inicial complicada.

**Uso básico**

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

Para aplicações reais, registrar logs apenas no console não é suficiente. Com o Loguru, você pode salvar logs em arquivos e configurar comportamentos avançados como rotação e retenção.

```python
logger.add("logs/app.log", rotation="500 MB", retention="10 days", compression="zip")

logger.info("Mensagem será salva no arquivo de log.")

```

**O que acontece?**

- Um novo arquivo será criado quando o tamanho exceder 500 MB.
- Logs mais antigos que 10 dias serão removidos automaticamente.
- Arquivos antigos são compactados para economizar espaço.

Essa configuração é ideal para sistemas que geram grandes volumes de logs, como pipelines de dados.


## Decoradores
<p align='center'>
    <img src='https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62cf81a1-f376-440a-83ff-83c144cce79b_1280x720.png' width=500>
</p>

Python é conhecido por sua simplicidade e poder, e uma de suas funcionalidades mais fascinantes são os decoradores. Eles são uma maneira de adicionar funcionalidade a funções ou métodos de forma elegante e concisa, sem alterar o código original.

No seu dia a dia, é comum encontrar situações em que você precisa reutilizar comportamentos, como registrar logs de execução, medir tempos de processamento ou validar entradas. Fazer isso manualmente em todas as funções não apenas gera redundância, mas torna o código menos legível. Decoradores resolvem esse problema de forma elegante, permitindo que você adicione funcionalidades extras de maneira reutilizável e organizada.

**Uso básico**

Um decorador é, basicamente, uma função que envolve outra função para modificar ou estender seu comportamento. Em Python, eles geralmente são implementados usando o símbolo `@` antes da função que você deseja decorar. Quando aplicados, eles executam uma lógica adicional antes ou depois da função decorada.

```python
def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Algo antes da função.")
        resultado = func(*args, **kwargs)
        print("Algo depois da função.")
        return resultado
    return wrapper

@meu_decorador
def minha_funcao():
    print("Executando a função principal.")

minha_funcao()
```

**Resultado**
```
Algo antes da função.
Executando a função principal.
Algo depois da função.
```

Por trás dos bastidores, os decoradores funcionam utilizando uma estrutura chamada wrapper. O wrapper é onde você insere a lógica adicional que será executada antes ou depois da função decorada. Ele utiliza *args e **kwargs, que são formas de capturar argumentos posicionais e nomeados, garantindo que qualquer função possa ser decorada, independentemente de sua assinatura.

## Loguru e decorators

<p align='center'>
    <img src='https://miro.medium.com/v2/resize:fit:1400/1*GNHA-Xcp7J9-hfNrhfI0cA.png' width=500>
</p>

Ao combinarmos Decoradores com o Loguru, que como já vimos é um dos frameworks mais populares para registro de logs em Python, eles se tornam uma solução prática e sofisticada para monitorar execuções, registrar erros e medir desempenho simplificando e melhorarando a qualidade do seu trabalho.

Erros são inevitáveis, mas perder rastreamentos críticos pode tornar a depuração uma tarefa assustadora. O Loguru simplifica isso com o decorador @logger.catch, que captura e registra automaticamente quaisquer exceções levantadas dentro de uma função.

**Uso básico**
```python
from loguru import logger

@logger.catch
def dividir(a, b):
    return a / b

# Exemplo de chamada
dividir(10, 0)
```
**Saída do Log:**
```
2024-11-22 14:30:00.123 | ERROR    | __main__:dividir:3 - ZeroDivisionError: division by zero
```
**Por que usar?**

- Captura automaticamente todos os erros dentro da função.
- Útil para funções críticas, como cálculos matemáticos ou operações de banco de dados.

Ao implementar esses conceitos, você melhora não só a eficiência, mas também a confiabilidade e a transparência do seu sistema. Experimente personalizar seus projetos e veja o impacto direto no seu dia a dia!
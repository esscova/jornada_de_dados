# Jornada de dados - Bootcamp Python: Parte I
## Fundamentos de Python para Engenharia de Dados

Se você está começando a aprender Python e quer entender como essa linguagem pode ser útil na sua jornada como engenheiro de dados, este repositório é para você. Python é uma das linguagens mais populares no mundo da engenharia de dados devido à sua simplicidade, versatilidade e vasta comunidade de suporte. Neste repositório, vamos explorar os fundamentos de Python com exemplos fáceis de entender, focados nos desafios mais comuns que você pode enfrentar ao trabalhar com dados.

O material deste repositório são exercícios, desafios ou materiais do meu treinamento na [Jornada de dados](https://suajornadadedados.com.br/).

## Índice

1. [A Linguagem Python](#a-linguagem-python)
2. [Tipos de Dados](#tipos-de-dados)
3. [Estruturas de Dados](#estruturas-de-dados)
4. [Inputs e Outputs com Python](#inputs-e-outputs-com-python)
5. [Controles de Fluxo: if, for, while](#controles-de-fluxo-if-for-while)
6. [TypeError, TypeCheck, TypeConversion](#typeerror-typecheck-typeconversion)
7. [TypeHints](#typehints)
8. [Abrindo Arquivos com `with`](#abrindo-arquivos-com-with)
9. [Try e Except](#try-e-except)

---

## A Linguagem Python

Python é uma linguagem de programação fácil de aprender e usar, com uma sintaxe clara e legível. Isso faz dela uma excelente escolha para iniciantes, especialmente na área de engenharia de dados, onde você vai lidar com grandes volumes de dados e realizar tarefas como limpeza e análise de dados.

Python é frequentemente usado em engenharia de dados para escrever scripts que automatizam tarefas, como importar e exportar dados de diferentes fontes, processar informações e integrá-las em sistemas de dados maiores.

### Exemplo básico:
```python
# Imprimir uma mensagem na tela
print("Olá, Engenharia de Dados!")
```
Neste exemplo simples, usamos a função `print()` para exibir uma mensagem. No dia a dia de um engenheiro de dados, você usará esse tipo de comando para visualizar resultados de processos ou verificar se os dados estão sendo manipulados corretamente.

Agora, vamos explorar os tipos de dados, que são fundamentais para trabalhar com qualquer tipo de dado em Python.

---

## Tipos de Dados

Python oferece uma variedade de tipos de dados, como inteiros, flutuantes, strings e listas, e cada um desses tipos é usado para representar diferentes tipos de informações.

### Exemplos comuns de tipos de dados:
```python
# Tipo inteiro
idade = 25

# Tipo flutuante
preco = 19.99

# Tipo string
nome = "João"

# Tipo lista
notas = [10, 8, 7.5, 9]
```

Na engenharia de dados, você frequentemente lidará com números (inteiros e flutuantes) e listas (que são ótimas para armazenar múltiplos valores, como notas de alunos ou valores de vendas).

À medida que você começa a manipular dados em arquivos ou bancos de dados, será essencial entender como converter tipos de dados. Isso nos leva ao próximo tópico: a conversão entre tipos de dados.

---

## Estruturas de Dados

Além dos tipos simples, Python também oferece estruturas de dados como listas, tuplas, dicionários e conjuntos. Essas estruturas são fundamentais quando você trabalha com grandes volumes de dados, pois elas permitem organizar e acessar os dados de maneira eficiente.

### Listas:
As listas são uma coleção de itens que podem ser modificados e acessados por índice. São bastante úteis em engenharia de dados quando você precisa armazenar coleções de dados que podem mudar ao longo do tempo.

```python
# Exemplo de lista de dados
clientes = ["João", "Maria", "Pedro"]

# Acessando um item da lista
print(clientes[1])  # Saída: Maria
```

### Dicionários:
Os dicionários armazenam dados no formato chave-valor, o que é útil quando você precisa associar um item a outro. Por exemplo, ao armazenar informações de clientes em um banco de dados, você poderia usar dicionários para associar o nome de um cliente ao seu e-mail ou telefone.

```python
# Exemplo de dicionário
cliente = {"nome": "João", "idade": 28}

# Acessando o valor associado à chave 'nome'
print(cliente["nome"])  # Saída: João
```

Essas estruturas são fundamentais para organizar dados em memória de maneira eficiente. Agora que vimos como organizar dados, vamos aprender a interagir com o usuário ou com arquivos para ler e escrever dados. Vamos explorar os **inputs e outputs** com Python.

---

## Inputs e Outputs com Python

Ao trabalhar com engenharia de dados, você frequentemente precisará ler dados de arquivos ou de usuários e depois salvar esses dados ou exibir resultados. Python fornece maneiras simples de fazer isso com a função `input()` para receber entradas e `print()` para exibir saídas.

### Exemplo de input:
```python
# Recebendo input do usuário
nome = input("Qual o seu nome? ")
print(f"Olá, {nome}!")
```

Além disso, Python permite que você leia e escreva arquivos, o que é uma habilidade crucial para qualquer engenheiro de dados.

### Exemplo de leitura e escrita de arquivos:
```python
# Lendo dados de um arquivo
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Gravando dados em um arquivo
with open("saida.txt", "w") as arquivo:
    arquivo.write("Processamento concluído com sucesso!")
```

Ler e gravar dados de arquivos é uma parte essencial de qualquer pipeline de dados, e a função `open()` em Python é a ferramenta que você usará para isso. Agora que sabemos como interagir com arquivos e o usuário, vamos dar uma olhada em como podemos controlar o fluxo do programa com base em condições e loops.

---

## Controles de Fluxo: if, for, while

Os **controles de fluxo** permitem que você defina a lógica de como seu programa deve se comportar com base em diferentes condições. Isso é essencial para tomar decisões durante o processamento dos dados.

### Exemplo de `if`:
```python
# Verificando se a idade de um cliente é maior que 18
idade = 20
if idade > 18:
    print("Cliente maior de idade")
else:
    print("Cliente menor de idade")
```

### Exemplo de `for` (loop):
```python
# Iterando sobre uma lista de clientes
clientes = ["João", "Maria", "Pedro"]
for cliente in clientes:
    print(cliente)
```

### Exemplo de `while` (loop):
```python
# Imprimindo números de 1 a 5 usando while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

Esses loops e condições são essenciais quando você precisa percorrer grandes conjuntos de dados ou aplicar lógicas específicas durante o processamento de informações.

Agora que vimos como controlar o fluxo do programa, vamos aprender sobre erros comuns que podem ocorrer e como tratá-los de maneira eficiente.

---

## TypeError, TypeCheck, TypeConversion

Ao manipular dados em Python, você pode acabar tentando realizar operações com tipos de dados incompatíveis, o que pode gerar erros. Em Python, os erros mais comuns relacionados a tipos são o `TypeError` e o `ValueError`.

### Exemplo de TypeError:
```python
# Tentando somar uma string com um número (isso causará um erro)
idade = "20"
salario = 3000
try:
    print(idade + salario)
except TypeError:
    print("Erro de tipo: não é possível somar uma string com um número.")
```

Além disso, é importante saber como **converter tipos de dados** quando necessário, por exemplo, converter uma string para um número inteiro.

### Exemplo de conversão de tipo:
```python
# Convertendo uma string para inteiro
idade = int("20")
print(idade + 10)  # Saída: 30
```

Essas habilidades são essenciais para garantir que seu código seja robusto e possa lidar com diferentes tipos de dados de maneira eficiente. Agora, vamos explorar como podemos usar **TypeHints** para tornar o código mais legível e fácil de entender.

---

## TypeHints

Os **TypeHints** são uma forma de adicionar anotações ao código para indicar que tipo de dados uma função espera receber e retornar. Embora Python seja uma linguagem dinâmica, os TypeHints ajudam a melhorar a clareza do código, especialmente quando o projeto cresce.

### Exemplo de TypeHint:
```python
# Usando TypeHints para indicar os tipos de dados
from typing import List

def calcular_media(notas: List[int]) -> float:
    return sum(notas) / len(notas)
```

Os TypeHints tornam o código mais fácil de ler, ajudando outros programadores a entender o que o código espera. Isso é especialmente importante em projetos de dados grandes, onde muitos dados diferentes precisam ser manipulados. Agora que aprendemos a usar TypeHints, vamos aprender como abrir arquivos de forma segura usando o `with`.

---

## Abrindo Arquivos com `with`

Quando se trabalha com arquivos grandes, como arquivos CSV ou logs, é importante garantir que os arquivos sejam fechados corretamente após o uso. O Python oferece a palavra-chave `with`, que facilita o trabalho com arquivos, garantindo que o arquivo seja fechado automaticamente após a leitura ou gravação.

### Exemplo de uso do `with`:

```python
# Lendo um arquivo com 'with' para garantir que seja fechado corretamente
with open("dados.csv", "r") as arquivo:
    dados = arquivo.readlines()
    print(dados)
```

Usar o `with` ao trabalhar com arquivos é uma boa prática, pois evita problemas relacionados a arquivos que não são fechados corretamente. Isso é especialmente importante quando estamos lidando com arquivos grandes, como registros de transações de banco de dados ou grandes volumes de dados em CSV, onde falhas podem resultar em desperdício de memória ou até mesmo corrupção dos dados.

---

## Try e Except

Erros e exceções podem ocorrer durante o processamento de dados, especialmente quando estamos lidando com grandes volumes de informações ou interagindo com fontes externas, como APIs ou bancos de dados. Python oferece o tratamento de exceções com `try` e `except`, permitindo capturar e lidar com erros de forma controlada.

### Exemplo de tratamento de erro:
```python
# Usando try-except para capturar erros ao tentar ler um arquivo
try:
    df = pd.read_csv('dados_input.csv')
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
```

Essa abordagem é extremamente útil em pipelines de dados, onde você pode precisar tratar falhas na leitura de arquivos ou na conexão com bancos de dados, garantindo que o processo continue funcionando, mesmo quando erros acontecem.

O uso do `try` e `except` ajuda a garantir que o código não falhe inesperadamente, oferecendo uma maneira de lidar com falhas de maneira controlada.

---

### Conclusão

Este repositório tem como objetivo fornecer uma base sólida para iniciantes em Python, especialmente focando em situações comuns enfrentadas por engenheiros de dados. Ao dominar esses fundamentos, você estará mais preparado para trabalhar com dados de maneira eficaz, desde o processamento de arquivos até a implementação de lógicas de fluxo de controle e tratamento de erros.

Python é uma linguagem poderosa e, com esses conceitos básicos, você estará bem equipado para começar a construir seus próprios scripts de automação de dados, manipular grandes volumes de dados e lidar com problemas que surgem durante o processamento e análise de dados.

Com o tempo, você vai perceber que, embora o Python seja uma linguagem simples, ele oferece ferramentas extremamente poderosas que são essenciais para qualquer engenheiro de dados. O próximo passo é continuar praticando e explorando mais profundamente as bibliotecas como Pandas, NumPy e outras ferramentas avançadas, que vão ampliar ainda mais suas capacidades no mundo da engenharia de dados.


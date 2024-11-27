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
6. [Funções em Python](#funções-em-python)
7. [TypeError, TypeCheck, TypeConversion](#typeerror-typecheck-typeconversion)
8. [TypeHints](#typehints)
9. [Abrindo Arquivos com `with`](#abrindo-arquivos-com-with)
10. [Try e Except](#try-e-except)

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

Essas estruturas são fundamentais para organizar dados em memória de maneira eficiente. Agora que sabemos como organizar dados, vamos aprender a interagir com o usuário ou com arquivos para ler e escrever dados. Vamos explorar os **inputs e outputs** com Python.

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

## Funções em Python

Funções são blocos de código que você pode definir uma vez e reutilizar em todo o seu programa. Elas ajudam a tornar o código mais modular e organizado, além de facilitar a reutilização de lógica.

Como engenheiro de dados, você vai criar funções para tarefas comuns, como carregar dados, limpar dados ou calcular métricas. Em Python, você pode definir funções usando a palavra-chave `def`.

### Exemplo básico de função:
```python
# Definindo uma função simples
def saudacao(nome):
    return f"Olá, {nome}!"

# Chamando a função
print(saudacao("João"))
```

Você pode passar diferentes parâmetros para funções, tornando-as flexíveis para diferentes situações. No contexto de engenharia de dados, isso é útil quando você precisa realizar a mesma operação em vários conjuntos de dados.

### Exemplo prático em Engenharia de Dados:
```python
import pandas as pd

# Função para carregar um arquivo CSV
def carregar_dados(caminho_arquivo):
    return pd.read_csv(caminho_arquivo)

# Carregando dados de um arquivo CSV
dados = carregar_dados("dados.csv")
print(dados.head())
```

Neste exemplo, a função `carregar_dados` encapsula a operação de carregar dados de um arquivo CSV, tornando seu código mais modular e reutilizável. Funções são essenciais para organizar e otimizar seu trabalho com dados em grandes projetos.

Agora, vamos falar sobre **TypeError**, **TypeCheck** e **TypeConversion**, que são conceitos importantes para garantir que seu código funcione corretamente.

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
print

(idade + 5)  # Saída: 25
```

---

## TypeHints

Em Python, as **dicas de tipo** (TypeHints) são usadas para indicar o tipo esperado de variáveis e parâmetros de funções. Isso ajuda a melhorar a legibilidade do código e facilita a detecção de erros.

### Exemplo de TypeHints:
```python
# Função com tipo de retorno especificado
def soma(a: int, b: int) -> int:
    return a + b
```

As dicas de tipo não alteram o comportamento do código, mas ajudam a documentar suas intenções e são especialmente úteis em projetos maiores, onde a clareza do código é essencial.

---

## Considerações finais
Neste repositório, exploramos conceitos fundamentais de Python para engenheiros de dados iniciantes. Desde os tipos de dados básicos até funções e tratamento de erros, você está agora mais preparado para lidar com os desafios do dia a dia, como manipulação de arquivos, automação de processos e limpeza de dados. Python é uma ferramenta poderosa, e com esses fundamentos, você está pronto para avançar para tarefas mais complexas.
# Métodos Getter e Setter: 

![](https://i.ytimg.com/vi/Sz9G0iwwHQI/hqdefault.jpg)

## O Caminho para Controlar o Acesso aos Atributos das Classes

Você já se perguntou como pode controlar a forma como acessamos ou modificamos os valores dentro de uma classe em Python? Vamos descobrir isso através de **métodos getter** e **setter** — ferramentas poderosas que ajudam a garantir que seus dados sejam manipulados corretamente. 

Imagina que você tem uma classe representando uma pessoa. Você quer garantir que o nome dessa pessoa seja composto apenas por letras e que sua idade não seja negativa. Como você faria isso? É aqui que entram os **getters** e **setters**. Eles funcionam como portas de entrada e saída para os atributos de uma classe. Ao invés de acessar ou modificar os valores diretamente, você os controla por meio desses métodos.

Vamos explorar o que são **getters** e **setters** e como você pode usá-los para garantir que os dados da sua classe sejam sempre válidos e bem estruturados.

---

### **O que São Getters e Setters?**

Em termos simples, **getters** são métodos usados para **obter** (ou ler) o valor de um atributo, enquanto **setters** são usados para **definir** (ou alterar) o valor de um atributo. Eles são especialmente úteis quando queremos adicionar algum tipo de **validação** ou **lógica extra** antes de permitir que o valor seja alterado ou lido.

Vamos quebrar isso em etapas simples:

- **Getter**: Um método que retorna o valor de um atributo.
- **Setter**: Um método que altera o valor de um atributo, com a possibilidade de validar ou modificar o valor antes de realmente alterá-lo.

### **Como Usar Getters e Setters em Python?**

Em Python, podemos usar o **decorador `@property`** para criar getters e setters de forma muito simples. O decorador `@property` transforma um método normal em um **getter**, e o **setter** é adicionado com o decorador `@nome_do_atributo.setter`.

Aqui está um exemplo básico para ilustrar:

#### **Exemplo 1: Produto com Preço**
Imaginemos uma classe `Produto` com um atributo `preco`. Queremos garantir que o preço nunca seja negativo.

```python
class Produto:
    def __init__(self, preco):
        self.__preco = preco  # Atributo privado

    @property
    def preco(self):
        """Getter: retorna o valor do preço."""
        return self.__preco

    @preco.setter
    def preco(self, preco):
        """Setter: garante que o preço nunca seja negativo."""
        if preco < 0:
            raise ValueError("O preço deve ser maior ou igual a zero.")
        self.__preco = preco
```

- O **getter** (`@property`) permite que você acesse o preço de forma segura.
- O **setter** (`@preco.setter`) permite modificar o preço, mas somente se ele for maior ou igual a zero.

Este tipo de abordagem ajuda a controlar o comportamento dos dados na sua classe e evita problemas como dados inconsistentes.

---

### **Por Que Usar Getters e Setters?**

Agora, você pode estar se perguntando: "Por que não simplesmente acessar ou alterar os atributos diretamente?" 

A principal razão é **encapsulamento**. Encapsular significa esconder os detalhes internos da implementação da classe, tornando os dados mais seguros e controláveis. Sem getters e setters, qualquer pessoa poderia alterar diretamente os atributos de uma classe, o que poderia levar a dados inválidos ou indesejados. Com getters e setters, você pode **validar** ou **modificar** os dados antes de permitir o acesso ou a alteração.

---

### **Exemplos Práticos de Getters e Setters em Pipelines de Arquivos**

Agora que já entendemos o básico dos getters e setters, vamos olhar para algumas situações reais em que esses métodos podem ser extremamente úteis — especialmente em **pipelines de arquivos**.

#### **Exemplo 2: Leitura e Escrita de Arquivos CSV**
Imagine que você está desenvolvendo um pipeline de dados que processa arquivos CSV. Você pode querer ter uma classe que encapsula a lógica de leitura de arquivos CSV e, ao mesmo tempo, garantir que os dados lidos estejam no formato esperado.

```python
import csv

class LeitorCSV:
    def __init__(self, caminho_arquivo):
        self.__caminho_arquivo = caminho_arquivo

    @property
    def caminho_arquivo(self):
        """Getter: Retorna o caminho do arquivo."""
        return self.__caminho_arquivo

    @caminho_arquivo.setter
    def caminho_arquivo(self, caminho):
        """Setter: Valida se o caminho é um arquivo CSV."""
        if not caminho.endswith(".csv"):
            raise ValueError("O arquivo deve ter a extensão .csv.")
        self.__caminho_arquivo = caminho

    def ler(self):
        """Método para ler o arquivo CSV"""
        with open(self.__caminho_arquivo, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
```

- O **getter** do caminho do arquivo (`caminho_arquivo`) permite que você acesse o caminho do arquivo CSV.
- O **setter** valida se o caminho fornecido tem a extensão `.csv`. Caso contrário, ele lança uma exceção.

#### **Exemplo 3: Controle de Dados em Arquivos JSON**
Agora, imagine que você está lidando com um arquivo JSON e deseja controlar as operações de leitura e escrita de forma segura.

```python
import json

class LeitorJSON:
    def __init__(self, caminho_arquivo):
        self.__caminho_arquivo = caminho_arquivo

    @property
    def caminho_arquivo(self):
        """Getter: Retorna o caminho do arquivo JSON."""
        return self.__caminho_arquivo

    @caminho_arquivo.setter
    def caminho_arquivo(self, caminho):
        """Setter: Valida se o caminho é um arquivo JSON."""
        if not caminho.endswith(".json"):
            raise ValueError("O arquivo deve ter a extensão .json.")
        self.__caminho_arquivo = caminho

    def ler(self):
        """Método para ler o arquivo JSON"""
        with open(self.__caminho_arquivo, 'r') as file:
            return json.load(file)
```

- O **getter** retorna o caminho do arquivo JSON, enquanto o **setter** garante que o arquivo tenha a extensão `.json`.
- Esse tipo de controle pode ser útil em pipelines de dados onde você precisa garantir que apenas arquivos de um tipo específico sejam processados.

---

### Encerramento e considerações finais

**Getters e Setters no Controle de Dados em Pipelines**

Como vimos, **getters e setters** são ferramentas poderosas para garantir a integridade e o controle dos dados em suas classes. Eles permitem que você valide e modifique os dados de forma segura antes de permitir o acesso ou a modificação direta.

Em pipelines de dados, como a leitura e escrita de arquivos CSV ou JSON, os getters e setters ajudam a **validar o formato de dados** e **prevenir erros** antes que eles afetem o fluxo de dados. Ao usar essas técnicas, você cria códigos mais robustos, seguros e fáceis de manter, minimizando riscos de falhas inesperadas nos seus processos.

Agora, você pode aplicar essas técnicas para criar pipelines de dados mais seguros e eficientes, além de proteger sua aplicação contra dados inválidos. Se você estiver lidando com dados em larga escala, como arquivos CSV ou JSON, considere o uso de getters e setters para melhorar o controle de qualidade dos seus dados e garantir a precisão dos resultados.
# Jornada de dados - Bootcamp Python: Parte III
## OOP - Programação com Orientação a Objetos em Python

A Programação Orientada a Objetos (OOP, do inglês Object-Oriented Programming) é um paradigma poderoso que permite organizar e estruturar código de maneira mais modular e reutilizável. Este repositório é focado em engenheiros de dados iniciantes que estão começando a explorar o conceito de OOP em Python e foi organizado conforme os meus estudos no treinamento em Python para engenheiros de dados da [Jornada de dados](https://suajornadadedados.com.br/). Vamos abordar desde os conceitos básicos de classes até técnicas mais avançadas, como herança, polimorfismo e encapsulamento, além de integrar bibliotecas úteis para facilitar tarefas comuns no dia a dia de um engenheiro de dados.

## Índice

1. [Diferenças entre os Paradigmas de Programação](#diferenças-entre-os-paradigmas-de-programação)
2. [Entendendo sobre Classes](#entendendo-sobre-classes)
3. [Criando Classes para Leitura de Arquivos](#criando-classes-para-leitura-de-arquivos)
4. [Classes com a Biblioteca Schedule](#classes-com-a-biblioteca-schedule)
5. [Subclasses da Classe ABC](#subclasses-da-classe-abc)
6. [Métodos Getter e Setter](#métodos-getter-e-setter)
7. [Métodos Especiais](#métodos-especiais)
8. [Utilizando a Biblioteca Faker para Gerar Dados de Testes](#utilizando-a-biblioteca-faker-para-gerar-dados-de-testes)
9. [Implementando Classe de Leitura de Arquivos com Método de Filtro por Atributo](#implementando-classe-de-leitura-de-arquivos-com-método-de-filtro-por-atributo)
10. [Avançando em Classes com Encapsulamento, Herança e Polimorfismo](#avançando-em-classes-com-encapsulamento-herança-e-polimorfismo)

---

## Diferenças entre os Paradigmas de Programação

Antes de começarmos a implementar classes e objetos, é importante entender a diferença entre os paradigmas de programação. O paradigma de programação em Python pode ser dividido em três principais abordagens:

1. **Programação Procedural**: Foca em escrever funções que operam sobre dados. A programação é baseada em sequência de instruções e não em entidades como objetos.
   
2. **Programação Orientada a Objetos (OOP)**: Organiza o código em torno de objetos, que são instâncias de classes. Objetos podem ter propriedades (atributos) e comportamentos (métodos). Esse paradigma facilita a reutilização de código e a manutenção de grandes sistemas.

3. **Programação Funcional**: Foca em funções puras, evitando estados mutáveis e efeitos colaterais. Em Python, podemos combinar OOP e programação funcional, o que dá flexibilidade e poder ao código.

Neste repositório, vamos nos concentrar na **Programação Orientada a Objetos** (OOP) com Python, que é a abordagem mais adequada para organizar projetos maiores e mais complexos.

---

## Entendendo sobre Classes

Em OOP, **classes** são a base para criar objetos. Elas definem as características e comportamentos dos objetos. Vamos entender como criar e utilizar classes em Python.

### Exemplo de uma classe simples:

```python
# Definindo uma classe chamada "Pessoa"
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto (instância) da classe "Pessoa"
pessoa1 = Pessoa("João", 25)
pessoa1.apresentar()  # Saída: Olá, meu nome é João e tenho 25 anos.
```

A classe `Pessoa` tem um **método construtor** (`__init__`) que é chamado quando criamos um novo objeto. Esse método define as propriedades (atributos) do objeto. O método `apresentar` é um comportamento que o objeto pode executar.

---

## Criando Classes para Leitura de Arquivos

Um caso prático de uso de classes em Python é a leitura e processamento de arquivos. Vamos criar uma classe que ajuda a ler dados de arquivos CSV.

### Exemplo de classe para ler arquivos:

```python
import csv

class LeitorCSV:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def ler_arquivo(self):
        with open(self.arquivo, mode='r') as file:
            leitor = csv.reader(file)
            for linha in leitor:
                print(linha)

# Criando um objeto da classe e lendo um arquivo CSV
leitor = LeitorCSV("dados.csv")
leitor.ler_arquivo()
```

Essa classe permite que você abra e leia os dados de um arquivo CSV, facilitando o processo de análise de dados.

---

## Classes com a Biblioteca Schedule

Uma biblioteca útil para automação de tarefas em Python é o **schedule**, que permite agendar a execução de funções de forma periódica. Vamos criar uma classe que utiliza essa biblioteca para agendar a execução de uma tarefa.

### Exemplo de uso da biblioteca schedule:

```python
import schedule
import time

class TarefaAgendada:
    def __init__(self, tarefa, intervalo):
        self.tarefa = tarefa
        self.intervalo = intervalo

    def agendar(self):
        schedule.every(self.intervalo).seconds.do(self.tarefa)
        while True:
            schedule.run_pending()
            time.sleep(1)

def minha_tarefa():
    print("Tarefa executada!")

# Criando e agendando a tarefa
tarefa = TarefaAgendada(minha_tarefa, 5)
tarefa.agendar()
```

Neste exemplo, a classe `TarefaAgendada` usa o `schedule` para agendar a execução da função `minha_tarefa` a cada 5 segundos.

---

## Subclasses da Classe ABC

Em Python, a classe **ABC** (Abstract Base Class) permite que você crie classes base abstratas, onde algumas funções são declaradas, mas não implementadas. As subclasses devem implementar essas funções.

### Exemplo de uso de ABC:

```python
from abc import ABC, abstractmethod

class ArquivoLeitura(ABC):
    @abstractmethod
    def ler(self):
        pass

class LeitorCSV(ArquivoLeitura):
    def ler(self):
        print("Lendo arquivo CSV...")

# Instanciando a classe LeitorCSV
leitor = LeitorCSV()
leitor.ler()  # Saída: Lendo arquivo CSV...
```

Neste exemplo, a classe `ArquivoLeitura` é uma classe abstrata e define um método `ler` que deve ser implementado pelas subclasses, como `LeitorCSV`.

---

## Métodos Getter e Setter

**Getters** e **setters** são métodos usados para acessar e modificar os atributos de uma classe de forma controlada. Eles são importantes para implementar o conceito de **encapsulamento** em OOP.

### Exemplo de getters e setters:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # O underscore indica um atributo privado
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if valor:
            self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self._idade = valor

# Usando os getters e setters
pessoa = Pessoa("Carlos", 30)
print(pessoa.nome)  # Saída: Carlos
pessoa.idade = 35
print(pessoa.idade)  # Saída: 35
```

Aqui, usamos o `@property` para definir os getters e `@nome.setter` para os setters, permitindo controlar o acesso aos atributos.

---

## Métodos Especiais

Métodos especiais, como `__str__`, `__repr__`, `__len__`, entre outros, permitem que você defina comportamentos personalizados para os objetos da sua classe. Eles são usados para operar de maneira mais intuitiva com objetos.

### Exemplo de método especial:

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} custa R${self.preco:.2f}"

produto = Produto("Café", 9.99)
print(produto)  # Saída: Café custa R$9.99
```

O método `__str__` define como o objeto será representado como string, o que é útil ao imprimir ou converter um objeto em uma string.

---

## Utilizando a Biblioteca Faker para Gerar Dados de Testes

A **biblioteca Faker** é uma ótima ferramenta para gerar dados falsos ou fictícios para testes, simulações e desenvolvimento. Isso é particularmente útil em engenharia de dados para gerar grandes volumes de dados de teste.

### Exemplo de uso do Faker:

```python
from faker import Faker

class GeradorDeDados:
    def __init__(self):
        self.faker = Faker()

    def gerar_usuario(self):
        return {
            "nome": self.faker.name(),
            "endereco": self.faker.address(),
            "email": self.faker.email()
        }

# Gerando dados fictícios
gerador = GeradorDeDados()
usuario = gerador.gerar_usuario()

print(usuario)
```

O `Faker` gera dados de teste como nomes, endereços e e-mails, o que facilita a simulação de entradas de dados em sistemas reais.

---

## Implementando Classe de Leitura de Arquivos com Método de Filtro por Atributo

Agora, vamos criar uma classe de leitura de arquivos CSV com a capacidade de filtrar os dados por atributos específicos.

### Exemplo de classe de leitura com filtro:

```python
import csv

class LeitorCSVComFiltro:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def filtrar_por_atributo(self, chave, valor):
        with open(self.arquivo, mode='r') as file:
            leitor = csv.DictReader(file)
            for linha in leitor:
                if linha[chave] == valor:
                    print(linha)

# Criando objeto e filtrando por um atributo
leitor = LeitorCSVComFiltro("dados.csv")
leitor.filtrar_por_atributo("cidade", "São Paulo")
```

Essa classe permite que você leia um arquivo CSV e aplique um filtro para exibir apenas os dados que correspondem a um determinado valor em um atributo.

---

## Avançando em Classes com Encapsulamento, Herança e Polimorfismo

Agora que entendemos o básico sobre classes, podemos explorar conceitos mais avançados da programação orientada a objetos: **encapsulamento**, **herança** e **polimorfismo**.

- **Encapsulamento**: Garante que os dados de uma classe estejam protegidos e só possam ser acessados de forma controlada, usando métodos públicos.
- **Herança**: Permite que uma classe herde atributos e métodos de outra classe.
- **Polimorfismo**: Permite que métodos em classes derivadas tenham o mesmo nome, mas comportamentos diferentes.

Esses conceitos tornam o código mais modular, reutilizável e flexível.

### Exemplo de herança e polimorfismo:

```python
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

# Testando o polimorfismo
animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.fazer_som())
```

Esse exemplo demonstra o polimorfismo, onde diferentes classes podem implementar o mesmo método com comportamentos distintos.

---

## Considerações finais

Neste repositório, exploramos como a **Programação Orientada a Objetos** em Python pode ser aplicada de maneira eficiente em engenharia de dados. Aprendemos a criar classes, utilizar bibliotecas poderosas, e implementamos conceitos avançados como herança e polimorfismo. Esses conhecimentos são essenciais para organizar e modularizar seu código, permitindo que você escreva sistemas mais eficientes e fáceis de manter.

Agora que você tem uma base de OOP em Python, pode aplicar esses conceitos em seus projetos de dados e automação, facilitando seu trabalho diário como engenheiro de dados.
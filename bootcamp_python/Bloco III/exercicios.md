# Bootcamp Python bloco III - OOP 
## Exercícios de Fixação

Cinco exercícios de fixação para cada subtema do repositório **OOP - Programação com Orientação a Objetos em Python**, com uma progressão de dificuldade para ajudar um engenheiro de dados iniciante a solidificar os conceitos.

---

### 1. **Diferenças entre os Paradigmas de Programação**

#### Exercício 1:
Liste e explique brevemente as diferenças entre programação **procedural** e **orientada a objetos** (OOP). Dê um exemplo simples de cada abordagem.

#### Exercício 2:
Crie um pequeno código para somar números de 1 a 10 utilizando a abordagem **procedural**. Em seguida, reescreva o código utilizando OOP. Compare os dois.

#### Exercício 3:
Explique o que é **programação funcional** e como ela se diferencia da **programação orientada a objetos**. Quando seria mais vantajoso usar OOP ao invés de programação funcional?

#### Exercício 4:
Dado um sistema de gerenciamento de usuários (nome e idade), implemente um código utilizando **programação procedural**. Depois, transforme o sistema para usar OOP, criando uma classe `Usuario`.

#### Exercício 5:
Imagine que você tem uma função que realiza a soma de duas variáveis. Implemente essa função no estilo **procedural**, depois refatore o código para utilizar **OOP** com um método dentro de uma classe.

---

### 2. **Entendendo sobre Classes**

#### Exercício 1:
Crie uma classe `Carro` com os atributos `marca`, `modelo` e `ano`. Adicione um método `mostrar_info()` que imprime as informações do carro.

#### Exercício 2:
Modifique a classe `Carro` para incluir um método que atualiza o ano do carro. Crie um objeto dessa classe e atualize o ano.

#### Exercício 3:
Implemente uma classe `Produto` com os atributos `nome`, `preço` e `quantidade`. Adicione um método `calcular_valor_total()` que retorna o valor total (preço * quantidade).

#### Exercício 4:
Crie uma classe `Pessoa` com os atributos `nome` e `idade`. Adicione um método `aniversario()` que aumenta a idade em 1 a cada vez que é chamado. Crie um objeto e simule o aniversário da pessoa.

#### Exercício 5:
Crie uma classe `Aluno` com os atributos `nome`, `nota1`, `nota2` e `nota3`. Adicione um método `calcular_media()` que retorna a média das notas. Teste a classe com alguns objetos.

---

### 3. **Criando Classes para Leitura de Arquivos**

#### Exercício 1:
Crie uma classe `LeitorTXT` que recebe um caminho de arquivo como parâmetro e imprime o conteúdo do arquivo. Crie um arquivo de teste e utilize a classe para ler esse arquivo.

#### Exercício 2:
Modifique a classe `LeitorTXT` para incluir um método que conta o número de linhas no arquivo. Teste a classe com diferentes arquivos.

#### Exercício 3:
Crie uma classe `LeitorCSV` que utiliza a biblioteca `csv` para ler um arquivo CSV e imprime os dados de cada linha. Teste com um arquivo CSV de exemplo.

#### Exercício 4:
Implemente um método na classe `LeitorCSV` para buscar um valor específico em uma coluna do arquivo CSV. Teste com um arquivo que tenha várias colunas.

#### Exercício 5:
Crie uma classe `LeitorJSON` que leia um arquivo JSON e extraia informações específicas do arquivo, como um nome ou id. Teste com um arquivo JSON de exemplo.

---

### 4. **Classes com a Biblioteca Schedule**

#### Exercício 1:
Crie uma classe `Tarefa` que imprime uma mensagem na tela a cada 10 segundos usando a biblioteca `schedule`.

#### Exercício 2:
Modifique a classe `Tarefa` para que ela aceite uma função como parâmetro, permitindo que você agende diferentes tipos de tarefas.

#### Exercício 3:
Implemente uma classe `Agendador` que receba várias tarefas e execute-as de acordo com um intervalo específico. Use a biblioteca `schedule` para agendar as tarefas.

#### Exercício 4:
Crie uma classe `TarefaComHoraEspecifica` que execute uma tarefa em um horário fixo. Por exemplo, execute uma tarefa às 14:00 horas todos os dias.

#### Exercício 5:
Implemente um sistema de agendamento que leia tarefas de um arquivo de texto e as agende automaticamente. Use a biblioteca `schedule` para executar essas tarefas periodicamente.

---

### 5. **Subclasses da Classe ABC**

#### Exercício 1:
Crie uma classe abstrata `FormaGeometrica` com um método abstrato `area()`. Depois, crie duas subclasses: `Circulo` e `Retangulo`, que implementam o método `area()`.

#### Exercício 2:
Implemente uma classe abstrata `Animal` com um método abstrato `fazer_som()`. Crie duas subclasses: `Cachorro` e `Gato`, que implementam o método `fazer_som()` com sons diferentes.

#### Exercício 3:
Crie uma classe abstrata `Arquivo` com um método abstrato `ler()`. Em seguida, crie duas subclasses: `LeitorCSV` e `LeitorJSON`, que implementam o método `ler()` de maneiras diferentes.

#### Exercício 4:
Implemente uma classe abstrata `Veiculo` com um método abstrato `acelerar()`. Crie subclasses como `Carro` e `Bicicleta` e implemente o comportamento do método `acelerar()` de forma distinta para cada uma.

#### Exercício 5:
Crie uma classe abstrata `ContaBancaria` com os métodos `depositar()` e `sacar()`. Implemente subclasses como `ContaCorrente` e `ContaPoupanca`, customizando as regras de cada tipo de conta.

---

### 6. **Métodos Getter e Setter**

#### Exercício 1:
Crie uma classe `Produto` com um atributo `preco`. Adicione um método getter e setter para acessar e modificar o preço, garantindo que o preço não seja negativo.

#### Exercício 2:
Implemente um getter e setter para o atributo `nome` de uma classe `Pessoa`. O setter deve garantir que o nome não contenha números ou caracteres especiais.

#### Exercício 3:
Crie uma classe `ContaBancaria` com um atributo `saldo`. Adicione métodos getter e setter para manipular o saldo, garantindo que o saldo nunca fique negativo.

#### Exercício 4:
Implemente um getter e setter para o atributo `idade` de uma classe `Pessoa`, onde o setter só deve permitir valores maiores que 0.

#### Exercício 5:
Crie uma classe `Produto` com um atributo `quantidade`. Adicione um método getter e setter para controlar a quantidade, garantindo que ela não seja um valor negativo e que a quantidade mínima seja 1.

---

### 7. **Métodos Especiais**

#### Exercício 1:
Crie uma classe `Produto` e implemente o método especial `__str__` para representar o produto como uma string com nome e preço formatado.

#### Exercício 2:
Implemente um método especial `__repr__` na classe `Produto` para que a representação da instância seja mais técnica, mostrando o tipo e os atributos.

#### Exercício 3:
Crie uma classe `Aluno` e implemente o método `__len__` para retornar o número de disciplinas que o aluno está matriculado.

#### Exercício 4:
Implemente o método especial `__add__` em uma classe `Produto` para permitir somar os preços de dois produtos.

#### Exercício 5:
Implemente um método especial `__eq__` na classe `Produto` para comparar se dois produtos são iguais (considerando o mesmo nome e preço).

---

### 8. **Utilizando a Biblioteca Faker para Gerar Dados de Testes**

#### Exercício 1:
Crie uma classe `GeradorDeDados` que usa a biblioteca `Faker` para gerar um nome e um endereço aleatório.

#### Exercício 2:
Implemente um método na classe `GeradorDeDados` para gerar um e-mail falso com a ajuda do `Faker`.

#### Exercício 3:
Crie uma classe `BancoDeDadosFalso` que gera uma lista de 10 usuários com nome, idade e e-mail utilizando a biblioteca `Faker`.

#### Exercício 4:
Crie uma classe `GeradorDeProdutos` que usa o `Faker` para gerar um nome de produto, preço e descrição. Gere uma lista de 5 produtos fictícios.

#### Exercício 5:
Implemente uma classe `GeradorDeVendas` que cria dados de vendas, como o nome do cliente, o produto adquirido e a data da venda, utilizando o `Faker`.

---

### 9. **Implementando Classe de Leitura de Arquivos com Método de Filtro por Atributo**

#### Exercício 1:
Crie uma classe `LeitorCSV` que leia um arquivo CSV e permita filtrar os dados por um valor específico em uma coluna.

#### Exercício 2:
Modifique a classe `LeitorCSV` para filtrar dados de um arquivo CSV com base em múltiplos atributos. Por exemplo, filtrar por "nome" e "idade".

#### Exercício 3:
Implemente um método na classe `LeitorCSV` que permita ordenar os dados de um arquivo CSV com

 base em uma coluna específica.

#### Exercício 4:
Crie uma classe `LeitorJSON` que leia um arquivo JSON e permita filtrar os dados por um valor em um campo específico.

#### Exercício 5:
Implemente uma classe `LeitorCSV` que permita filtrar e salvar os dados filtrados em um novo arquivo CSV.
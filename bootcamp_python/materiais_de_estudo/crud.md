## CRUD em Python

![](https://miro.medium.com/v2/resize:fit:1400/1*2eBdh0vLZjUyCDF6x1EqvQ.png)

**Fundamentos Essenciais para Engenheiros de Dados Iniciantes**

Se você já se perguntou como os sistemas de banco de dados conseguem organizar e manipular dados de forma eficiente, a resposta está em um conjunto de operações simples, mas poderosas: **CRUD**. Estas operações são a base para qualquer interação com dados em um banco de dados e representam a espinha dorsal de sistemas de informação. Vamos explorar cada uma delas com exemplos práticos em Python, para que você entenda como funcionam e como pode usá-las no seu trabalho.

---

## **1. O que é CRUD?**

Antes de mergulharmos no código, é importante entender o que significa **CRUD**. O acrônimo representa quatro operações fundamentais que podemos realizar com dados:

- **C** (Create): Criar novos dados.
- **R** (Read): Ler ou consultar dados existentes.
- **U** (Update): Atualizar dados que já existem.
- **D** (Delete): Excluir dados.

Essas operações formam o alicerce de qualquer sistema que envolva armazenamento de dados, seja em um banco de dados, um arquivo ou até mesmo uma simples lista em Python. A melhor maneira de entender essas operações é praticando. Por isso, vamos usar um exemplo simples com listas em Python, simulando a interação com um banco de dados.

---

## **2. CRUD com Listas em Python**

Para começar, vamos imaginar que temos uma lista de usuários e queremos manipular esses dados da forma mais simples possível. Aqui, vamos simular o CRUD utilizando uma lista de dicionários, onde cada dicionário representa um usuário.

```python
# Lista de usuários (simulando um banco de dados simples)
usuarios = [
    {"id": 1, "nome": "João", "idade": 30},
    {"id": 2, "nome": "Maria", "idade": 25},
    {"id": 3, "nome": "Carlos", "idade": 35}
]

# CREATE: Adicionando um novo usuário
novousuario = {"id": 4, "nome": "Ana", "idade": 28}
usuarios.append(novousuario)

# READ: Lendo (consultando) os dados de um usuário
usuario = next((u for u in usuarios if u["id"] == 2), None)

# UPDATE: Atualizando as informações de um usuário
usuario = next((u for u in usuarios if u["id"] == 1), None)
if usuario:
    usuario["idade"] = 31  # Alterando a idade de João

# DELETE: Excluindo um usuário
usuarios = [u for u in usuarios if u["id"] != 3]  # Remover Carlos

# Exibindo a lista de usuários atualizada
print(usuarios)

```

Neste exemplo, cada operação CRUD é ilustrada de forma simples:

- **CREATE**: Adicionamos um novo usuário à lista.
- **READ**: Consultamos os dados de um usuário específico, buscando pelo `id`.
- **UPDATE**: Alteramos a idade de um usuário.
- **DELETE**: Excluímos um usuário da lista.

Essas operações podem ser realizadas em qualquer tipo de dado em Python, mas quando falamos de sistemas reais, como bancos de dados, as coisas ficam um pouco mais complexas. Vamos ver como isso funciona em um banco de dados real.

---

## **3. CRUD com Banco de Dados: Usando SQLite**

Agora que você entende as operações CRUD em listas, vamos dar um passo à frente e ver como essas operações são feitas em um banco de dados real, como o **SQLite**. O SQLite é um banco de dados leve e integrado ao Python, perfeito para aprender e testar operações em bancos de dados relacionais.

O processo de manipulação de dados em um banco de dados real segue a mesma lógica, mas com alguns detalhes adicionais. Vamos criar um banco de dados simples e realizar as operações CRUD usando o SQLite.

```python
import sqlite3

# Criando uma conexão com o banco de dados (se o banco não existir, ele será criado)
conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

# Criando a tabela de usuários (equivalente ao schema no banco de dados)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

# 1. CREATE: Adicionando um novo usuário no banco de dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("João", 30))
conn.commit()

# 2. READ: Consultando os dados de um usuário específico
cursor.execute("SELECT * FROM usuarios WHERE id = ?", (1,))
usuario = cursor.fetchone()  # Recupera a primeira linha (se existir)
print(usuario)

# 3. UPDATE: Atualizando os dados de um usuário
cursor.execute("UPDATE usuarios SET idade = ? WHERE id = ?", (31, 1))
conn.commit()

# 4. DELETE: Excluindo um usuário do banco de dados
cursor.execute("DELETE FROM usuarios WHERE id = ?", (1,))
conn.commit()

# Fechando a conexão
conn.close()

```

Como você pode ver, as operações CRUD no banco de dados são muito semelhantes às realizadas nas listas em Python. Contudo, ao usar o SQLite:

- **CREATE** é feito com a instrução `INSERT INTO`.
- **READ** utiliza o `SELECT`.
- **UPDATE** usa o `UPDATE`.
- **DELETE** é feito através do `DELETE`.

Essas operações são a base para qualquer interação com dados em um banco de dados, mas também é importante entender como elas podem ser otimizadas e protegidas.

---

## **4. Exemplos Práticos de CRUD para Engenheiros de Dados**

Agora que vimos como implementar o CRUD em Python e com bancos de dados relacionais, vamos explorar exemplos mais específicos e relevantes para engenheiros de dados.

## **Exemplo 1: Atualizando Dados em um Pipeline de ETL**

Imagine que você está construindo um pipeline de ETL (Extract, Transform, Load) e precisa atualizar registros de um banco de dados com novos dados extraídos de fontes externas. Aqui está como você pode usar **UPDATE** de forma eficiente:

```python
import sqlite3

# Conexão com o banco de dados de produção
conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

# Supomos que recebemos um DataFrame com dados atualizados
# e precisamos atualizar a tabela de produtos
dados_atualizados = [
    (100, 'Produto A', 200),  # id, nome, novo_estoque
    (102, 'Produto B', 150),
]

# Atualizando o estoque dos produtos
for produto in dados_atualizados:
    cursor.execute("UPDATE produtos SET estoque = ? WHERE id = ?", (produto[2], produto[0]))
conn.commit()

# Fechar a conexão
conn.close()

```

Neste exemplo, você está pegando dados de uma fonte externa (um DataFrame ou arquivo CSV) e realizando um **UPDATE** no banco de dados para atualizar o estoque de produtos. Esse tipo de tarefa é comum quando você precisa manter o banco de dados sincronizado com as últimas informações de sistemas externos.

## **Exemplo 2: Excluindo Dados Duplicados em uma Tabela de Dados de Logs**

Em muitos casos, durante a ingestão de dados, é comum que dados duplicados sejam inseridos no banco de dados. Um engenheiro de dados pode usar **DELETE** para remover esses registros:

```python
import sqlite3

# Conexão com o banco de dados de logs
conn = sqlite3.connect('logs.db')
cursor = conn.cursor()

# Excluindo logs duplicados (baseado no ID e timestamp)
cursor.execute('''
    DELETE FROM logs WHERE rowid NOT IN (
        SELECT MIN(rowid) FROM logs GROUP BY id, timestamp
    )
''')
conn.commit()

# Fechar a conexão
conn.close()

```

Aqui, estamos removendo duplicatas de uma tabela de logs. Usamos uma subconsulta para manter apenas o primeiro registro de cada grupo de logs duplicados, com base no campo `id` e `timestamp`.

## **Exemplo 3: Criando um Novo Registro de Dados em Uma Tabela de Clientes**

Durante a ingestão de dados de novos clientes, é comum usar a operação **CREATE** para inserir esses dados em um banco de dados:

```python
import sqlite3

# Conexão com o banco de dados de clientes
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# Dados de um novo cliente
novo_cliente = ("Carlos Silva", "carlos@email.com", "Rua A, 123")

# Inserindo o novo cliente na tabela
cursor.execute("INSERT INTO clientes (nome, email, endereco) VALUES (?, ?, ?)", novo_cliente)
conn.commit()

# Fechar a conexão
conn.close()

```

Esse exemplo é uma operação básica de inserção de dados. Em sistemas de dados reais, esse tipo de operação é repetido frequentemente, especialmente quando se trata de ingestão de novos dados em sistemas de CRM, plataformas de e-commerce ou bancos de dados transacionais.

---

## **5. Práticas e Considerações Importantes**

Agora que vimos alguns exemplos específicos, vale a pena discutir algumas práticas essenciais para garantir que seu código

seja eficiente e seguro ao trabalhar com dados:

- **Validação de Dados**: Antes de fazer qualquer operação, sempre valide os dados para garantir que estão no formato correto.
- **SQL Injection**: Ao interagir com bancos de dados, use sempre parâmetros nas consultas, como demonstrado no exemplo com `?`. Isso protege contra ataques de injeção SQL.
- **Transações**: Em sistemas mais complexos, use transações para garantir que múltiplas operações sejam atômicas (todas ou nenhuma).

Essas boas práticas são fundamentais quando você começa a trabalhar com bancos de dados reais, especialmente em ambientes de produção.

---

## **6. Conclusão e Próximos Passos**

Agora que você tem uma boa compreensão das operações CRUD em Python e como elas se aplicam a bancos de dados reais, você está pronto para explorar mais sobre como otimizar essas operações. A próxima etapa seria aprender a trabalhar com bancos de dados maiores e mais complexos, como MySQL ou PostgreSQL, e como lidar com grandes volumes de dados de maneira eficiente.

Com esses exemplos específicos para engenheiros de dados, esperamos ter ilustrado de forma prática como as operações CRUD são aplicadas no dia a dia, em tarefas como integração de dados, manutenção de registros e otimização de processos de ingestão de dados.
import sqlite3
from faker import Faker
from datetime import datetime, timedelta
from pathlib import Path
import random
import csv
import os

# configs
BD_URL = Path("data")/"clientes2.db"
faker = Faker()

# PARTE I - FUNÇÕES PARA CRIAR E POPULAR BD

def conectar_bd():
    conn = sqlite3.connect(BD_URL)
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela():
    conn, cursor = conectar_bd()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            endereco TEXT,
            telefone TEXT,
            data_cadastro TEXT
        )
    ''')
    conn.commit()
    conn.close()


def popular_tabela(quantidade=10):
    conn, cursor = conectar_bd()
    for _ in range(quantidade):
        nome = faker.name()
        email = faker.email()
        endereco = faker.address()
        telefone = faker.phone_number()
        data_cadastro = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT INTO clientes (nome, email, endereco, telefone, data_cadastro)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, email, endereco, telefone, data_cadastro))
    conn.commit()
    conn.close()


# PARTE II - RESOLVENDO EXERCÍCIOS

## 1. Listagem de registros
def listar_clientes():
    conn, cursor = conectar_bd()
    cursor.execute('''
                SELECT id, nome, email, telefone, data_cadastro
                FROM clientes
                ''')
    clientes = cursor.fetchall()
    conn.close()
    for cliente in clientes:
        print(cliente)

## 2. busca de um cliente por email
def buscar_cliente_email(email):
    conn, cursor = conectar_bd()
    cursor.execute('''
                SELECT *
                FROM clientes
                WHERE email = ?
                ''', (email,))
    cliente = cursor.fetchone()
    conn.close()
    return cliente

## 3. Busca de um cliente por id
def buscar_cliente_id(id):
    conn, cursor = conectar_bd()
    cursor.execute('''
                SELECT *
                FROM clientes
                WHERE id = ?
                ''', (id,))
    cliente = cursor.fetchone()
    conn.close()
    return cliente

## 4. atualização de um cliente
def atualizar_cliente(id, novo_endereco, novo_telefone):
    conn, cursor = conectar_bd()
    cursor.execute(
        '''
        UPDATE clientes
        SET endereco = ?, telefone = ?
        WHERE id = ?
        ''', 
        (novo_endereco, novo_telefone, id)
    )
    conn.commit()
    conn.close()

## 5. exclusão de um cliente
def deletar_cliente(id):
    conn, cursor = conectar_bd()
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
    conn.commit()
    conn.close()

## 6. listagem de clientes por periodo
def listar_clientes_por_periodo(data_inicio, data_fim):
    conn, cursor = conectar_bd()
    cursor.execute('''
        SELECT id, nome, email, telefone, data_cadastro
        FROM clientes
        WHERE data_cadastro BETWEEN ? AND ?
    ''', (data_inicio, data_fim))
    clientes = cursor.fetchall()
    conn.close()
    for cliente in clientes:
        print(cliente)

## 7. busca com paginação
def lista_clientes_paginacao(pagina=1, tamanho=5):
    conn, cursor = conectar_bd()
    offset = (pagina-1)*tamanho
    cursor.execute('''
        SELECT id, nome, email, telefone, data_cadastro
        FROM clientes
        LIMIT ? OFFSET ?
    ''', (tamanho, offset))
    clientes = cursor.fetchall()
    conn.close()
    for cliente in clientes:
        print(cliente)

# 8. busca de clientes com emails duplicados
def buscar_emails_duplicados():
    conn, cursor = conectar_bd()
    cursor.execute('''
        SELECT email, COUNT(*) as quantidade
        FROM clientes
        GROUP BY email
        HAVING COUNT(*) > 1
    ''')
    emails_duplicados = cursor.fetchall()
    conn.close()
    
    if emails_duplicados:
        print("Emails duplicados encontrados:")
        for email, quantidade in emails_duplicados:
            print(f"Email: {email}, Ocorrências: {quantidade}")
    else:
        print("Nenhum email duplicado encontrado.")
    
    return emails_duplicados

## 9. exportando para csv
def exportar_clientes_csv():
    conn, cursor = conectar_bd()
    cursor.execute('''
        SELECT id, nome, email, telefone, data_cadastro
        FROM clientes
    ''')
    clientes = cursor.fetchall()
    conn.close()
    
    directory = 'data'
    file_path = os.path.join(directory, 'clientes.csv')
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'nome', 'email', 'telefone', 'data_cadastro'])
        writer.writerows(clientes)
    
    print(f'Arquivo {file_path} criado com sucesso!')

# PARTE III - INTERACAO COM O USUARIO
def main():
    criar_tabela()
    popular_tabela()
    while True:
        print("\nSistema de Gerenciamento de Clientes")
        print("1 - Listar Clientes")
        print("2 - Buscar Cliente por Email")
        print("3 - Buscar Cliente por ID")
        print("4 - Atualizar Cliente")
        print("5 - Excluir Cliente")
        print("6 - Listar Clientes por Periodo")
        print("7 - Listar Clientes com Paginação")
        print("8 - Buscar Emails Duplicados")
        print("9 - Exportar Clientes para CSV")
        print("10 - Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            listar_clientes()

        elif opcao == "2":
            email = input("Digite o email do cliente: ")
            cliente = buscar_cliente_email(email)
            if cliente:
                print(cliente)
            else:
                print("Cliente nao encontrado.")

        elif opcao == "3":
            id = input("Digite o ID do cliente: ")
            cliente = buscar_cliente_id(id)
            if cliente:
                print(cliente)
            else:
                print("Cliente nao encontrado.")

        elif opcao == "4":
            id = input("Digite o ID do cliente: ")
            novo_endereco = input("Digite o novo endereco: ")
            novo_telefone = input("Digite o novo telefone: ")
            atualizar_cliente(id, novo_endereco, novo_telefone)
            print("Cliente atualizado com sucesso!")

        elif opcao == "5":
            id = input("Digite o ID do cliente: ")
            deletar_cliente(id)
            print("Cliente excluido com sucesso!")

        elif opcao == "6":
            data_inicio = input("Digite a data de inicio (YYYY-MM-DD): ")
            data_fim = input("Digite a data de fim (YYYY-MM-DD): ")
            listar_clientes_por_periodo(data_inicio, data_fim)

        elif opcao == "7":
            pagina = int(input("Digite a pagina: "))
            tamanho = int(input("Digite o tamanho: "))
            lista_clientes_paginacao(pagina, tamanho)

        elif opcao == "8":
            buscar_emails_duplicados()

        elif opcao == "9":
            exportar_clientes_csv()

        elif opcao == "10":
            break

        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()
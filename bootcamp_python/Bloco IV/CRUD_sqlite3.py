import sqlite3
from datetime import datetime
from pathlib import Path

# configs
BD_URL = Path('data')/'filmes.sqlite3'

def conectar_bd():
    conn = sqlite3.connect(BD_URL)
    cursor = conn.cursor()
    return conn, cursor

def criar_banco_dados():
    conn, cursor = conectar_bd()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            genero TEXT,
            created_at TEXT,
            updated_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

##########################################################
# PARTE I - FUNÇÕES PARA INTERAGIR COM O BANCO DE DADOS
#########################################################

def criar_filme(titulo, ano, genero):
    conn, cursor = conectar_bd()
    created_at = updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(
        "INSERT INTO filmes (titulo, ano, genero, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
        (titulo, ano, genero, created_at, updated_at)
    )
    conn.commit()
    conn.close()

def listar_filmes():
    conn, cursor = conectar_bd()
    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall()
    conn.close()
    return filmes

def listar_filme_id(id):
    conn, cursor = conectar_bd()
    cursor.execute("SELECT * FROM filmes WHERE id = ?", (id,))
    filme = cursor.fetchone()
    conn.close()
    return filme

def atualizar_filme(id, novos_dados):
    conn, cursor = conectar_bd()
    filme = listar_filme_id(id)
    if filme:
        updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        novo_titulo = novos_dados.get("titulo", filme[1]) or filme[1]
        novo_ano = novos_dados.get("ano", filme[2]) or filme[2]
        novo_genero = novos_dados.get("genero", filme[3]) or filme[3]
        cursor.execute(
            """
            UPDATE filmes
            SET titulo = ?, ano = ?, genero = ?, updated_at = ?
            WHERE id = ?
            """,
            (novo_titulo, novo_ano, novo_genero, updated_at, id)
        )
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

def deletar_filme(id):
    conn, cursor = conectar_bd()
    cursor.execute("DELETE FROM filmes WHERE id = ?", (id,))
    conn.commit()
    conn.close()

##########################################################
# PARTE II - FUNÇÃO PRINCIPAL INTERAÇÃO COM USUÁRIO
#########################################################

def main():
    criar_banco_dados()
    while True:
        print("\nSistema de Gerenciamento de Filmes")
        print("1 - Criar Filme")
        print("2 - Listar Filmes")
        print("3 - Atualizar Filme")
        print("4 - Deletar Filme")
        print("5 - Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do filme: ")
            try:
                ano = int(input("Digite o ano do filme: "))
                genero = input("Digite o gênero do filme: ")
                criar_filme(titulo, ano, genero)
                print("Filme criado com sucesso!")
            except ValueError:
                print("Ano deve ser um número válido.")

        elif opcao == "2":
            filmes = listar_filmes()
            for filme in filmes:
                print(f"ID: {filme[0]}, Título: {filme[1]}, Ano: {filme[2]}, Gênero: {filme[3]}, Criado em: {filme[4]}")

        elif opcao == "3":
            try:
                id = int(input("Digite o ID do filme a ser atualizado: "))
                titulo = input("Novo título (deixe vazio para manter): ")
                ano = input("Novo ano (deixe vazio para manter): ")
                genero = input("Novo gênero (deixe vazio para manter): ")
                novos_dados = {
                    "titulo": titulo or None,
                    "ano": int(ano) if ano else None,
                    "genero": genero or None
                }
                if atualizar_filme(id, novos_dados):
                    print("Filme atualizado com sucesso!")
                else:
                    print("Filme não encontrado.")
            except ValueError:
                print("ID ou ano inválido.")


        elif opcao == "4":
            try:
                id = int(input("Digite o ID do filme a ser deletado: "))
                deletar_filme(id)
                print("Filme deletado com sucesso!")
            except ValueError:
                print("ID inválido.")

        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from pathlib import Path

# Configs
BD_URL = f"sqlite:///{Path('data') / 'filmes_sqlalchemy.db'}"
engine = create_engine(BD_URL, echo=False)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# classe base
class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    genero = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

##########################################################
# PARTE I - FUNÇÕES PARA INTERAGIR COM O BANCO DE DADOS
#########################################################

def criar_banco_dados():
    Base.metadata.create_all(bind=engine)

def criar_filme(session, titulo, ano, genero):
    novo_filme = Filme(titulo=titulo, ano=ano, genero=genero)
    session.add(novo_filme)
    session.commit()
    session.refresh(novo_filme)
    return novo_filme

def listar_filmes(session):
    return session.query(Filme).all()

def listar_filme_por_id(session, id):
    return session.query(Filme).filter(Filme.id == id).first()

def atualizar_filme(session, id, novos_dados):
    filme = listar_filme_por_id(session, id)
    if filme:
        filme.titulo = novos_dados.get("titulo", filme.titulo) or filme.titulo
        filme.ano = novos_dados.get("ano", filme.ano) or filme.ano
        filme.genero = novos_dados.get("genero", filme.genero)
        filme.updated_at = datetime.now()
        session.commit()
        return filme
    return None



def deletar_filme(session, id):
    filme = listar_filme_por_id(session, id)
    if filme:
        session.delete(filme)
        session.commit()
        return True
    return False

def main():
    criar_banco_dados()
    session = SessionLocal()
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
                criar_filme(session, titulo, ano, genero)
                print("Filme criado com sucesso!")
            except ValueError:
                print("Ano deve ser um número válido.")

        elif opcao == "2":
            filmes = listar_filmes(session)
            for filme in filmes:
                print(f"ID: {filme.id}, Título: {filme.titulo}, Ano: {filme.ano}, Gênero: {filme.genero}, Criado em: {filme.created_at}")

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
                if atualizar_filme(session, id, novos_dados):
                    print("Filme atualizado com sucesso!")
                else:
                    print("Filme não encontrado.")
            except ValueError:
                print("ID ou ano inválido.")



        elif opcao == "4":
            try:
                id = int(input("Digite o ID do filme a ser deletado: "))
                if deletar_filme(session, id):
                    print("Filme deletado com sucesso!")
                else:
                    print("Filme não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "5":
            print("Encerrando o sistema...")
            session.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

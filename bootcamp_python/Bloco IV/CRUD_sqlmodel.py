from sqlmodel import SQLModel, Field, Session, create_engine, select
from datetime import datetime

# configs
engine = create_engine("sqlite:///data/filmes.db")
class Filme(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    titulo: str
    ano: int
    genero: str = None
    created_at: str = None
    updated_at: str = None

##########################################################
# PARTE I - FUNÇÕES PARA INTERAGIR COM O BANCO DE DADOS
#########################################################

def criar_banco_dados():
    SQLModel.metadata.create_all(engine)

def criar_filme(session: Session, filme: Filme):
    filme.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filme.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session.add(filme)
    session.commit()
    session.refresh(filme)
    return filme


def listar_filmes(session: Session):
    return session.exec(select(Filme)).all()


def listar_filme_id(session: Session, id: int):
    return session.exec(select(Filme).where(Filme.id == id)).first()


def atualizar_filme(session: Session, id: int, novos_dados: dict):
    filme = listar_filme_id(session, id)
    if filme:
        for key, value in novos_dados.items():
            if value:
                setattr(filme, key, value)
        filme.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        session.commit()
        session.refresh(filme)
        return filme
    return None


def deletar_filme(session: Session, id: int):
    filme = listar_filme_id(session, id)
    if filme:
        session.delete(filme)
        session.commit()

##########################################################
# PARTE II - FUNÇÃO PRINCIPAL INTERAÇÃO COM USUÁRIO
##########################################################

def main():
    criar_banco_dados()
    
    with Session(engine) as session:
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
                    filme = criar_filme(session, Filme(titulo=titulo, ano=ano, genero=genero))
                    print(f"Filme {filme.titulo} criado com sucesso!")
                except ValueError:
                    print("Ano deve ser um número válido.")

            elif opcao == "2":
                filmes = listar_filmes(session)
                for filme in filmes:
                    print(f"ID: {filme.id}, Título: {filme.titulo}, Ano: {filme.ano}, Gênero: {filme.genero}, Criado em: {filme.created_at}")

            elif opcao == "3":
                try:
                    id = int(input("Digite o ID do filme a ser atualizado: "))
                    filme = listar_filme_id(session, id)
                    if filme:
                        titulo = input(f"Novo título ({filme.titulo}): ") or filme.titulo
                        ano = input(f"Novo ano ({filme.ano}): ") or filme.ano
                        genero = input(f"Novo gênero ({filme.genero}): ") or filme.genero
                        novos_dados = {"titulo": titulo, "ano": int(ano), "genero": genero}
                        atualizar_filme(session, id, novos_dados)
                        print("Filme atualizado com sucesso!")
                    else:
                        print("Filme não encontrado.")
                except ValueError:
                    print("ID ou ano inválido.")

            elif opcao == "4":
                try:
                    id = int(input("Digite o ID do filme a ser deletado: "))
                    deletar_filme(session, id)
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

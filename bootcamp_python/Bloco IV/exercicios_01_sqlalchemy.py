####################################################################################################
# Conectando ao Banco de Dados e Criando um Modelo Simples
#
# Objetivo: Entender como conectar ao banco de dados e como criar um modelo (tabela) com SQLAlchemy.
#
# Tarefa:
#
# - Crie um banco de dados SQLite chamado `empresa.db`.
# - Defina uma tabela chamada `funcionarios` com as seguintes colunas:
#     - `id`: inteiro (chave primária).
#     - `nome`: texto (com limite de 100 caracteres).
#     - `cargo`: texto.
#     - `data_admissao`: data.
#     - `salario`: float.
#
# Use SQLAlchemy para configurar e criar essa tabela no banco de dados.
#
# Dicas:
#
# - Utilize a classe `Base` do SQLAlchemy.
# - Lembre-se de configurar a `engine` para o banco de dados e criar as tabelas.
###################################################################################################


from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///data/empresa.db')  # cria a engine para o banco de dados
Base = declarative_base()  # cria a classe base para as tabelas

# clase funcionario
class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    cargo = Column(String)
    data_admissao = Column(Date)
    salario = Column(Float)


# cria a tabela no banco de dados com base na classe
Base.metadata.create_all(engine)
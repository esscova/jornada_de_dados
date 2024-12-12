"""
Excluindo Dados

Objetivo: Excluir registros do banco de dados.

Tarefa:

- Apague todos os funcionários que foram admitidos antes de 2015.
- Confirme a exclusão de registros.

Dicas:

- Utilize o método `session.query().filter().delete()`.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from exercicios_sqlalchemy_01 import Funcionario
from datetime import datetime

engine = create_engine('sqlite:///data/empresa.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# excluindo um registr
data = datetime.strptime('2015-01-01', '%Y-%m-%d')
resgistros_excluidos = session.query(Funcionario).filter(Funcionario.data_admissao < data).delete()
session.commit()

print(resgistros_excluidos)
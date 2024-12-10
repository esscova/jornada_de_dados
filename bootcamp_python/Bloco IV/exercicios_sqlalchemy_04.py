"""
Atualizando Registros

Objetivo: Aprender a atualizar registros de maneira eficiente.

Tarefa:

- Atualize o salário de um funcionário específico (usando o `id`).
- Altere o cargo de todos os funcionários que ganham menos de R$ 30.000,00 para "Assistente".

Dicas:

- Utilize o método `session.query().filter().update()` para atualizações eficientes.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from exercicios_sqlalchemy_01 import Funcionario

engine = create_engine('sqlite:///data/empresa.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# atualizando um registro
funcionario = session.query(Funcionario).filter(Funcionario.id == 1).first()
funcionario.salario = 60000

# atualizando varios registros
session.query(Funcionario).filter(Funcionario.salario < 30000).update({'cargo': 'Assistente'})

session.commit()
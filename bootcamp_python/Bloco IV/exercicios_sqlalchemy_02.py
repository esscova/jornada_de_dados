"""
Inserindo Dados na Tabela

Objetivo: Inserir múltiplos registros de forma eficiente.

Tarefa:

- Crie ao menos 5 registros de funcionários com valores fictícios.
- Insira esses registros de forma eficiente usando o método `session.add_all()`.

Dicas:

- Utilize o método `session.commit()` para persistir os dados no banco.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from exercicios_sqlalchemy_01 import Funcionario
from faker import Faker
from datetime import datetime

faker = Faker()

engine = create_engine('sqlite:///data/empresa.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


funcionarios = [
    Funcionario(
        nome=faker.name(),
        cargo=faker.job(),
        data_admissao=datetime.strptime(faker.date(), '%Y-%m-%d').date(),  # converte para datetime ja que o faker gera strings
        salario=faker.random_number(digits=5)
    )
    for _ in range(5)
]

session.add_all(funcionarios)
session.commit()
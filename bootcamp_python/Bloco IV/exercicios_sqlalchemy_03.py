"""
Consultando Dados

Objetivo: Realizar consultas simples no banco de dados utilizando filtros.

Tarefa:

- Recupere todos os funcionários com um salário superior a R$ 50.000,00.
- Ordene os resultados pela data de admissão, do mais recente para o mais antigo.

Dicas:

- Utilize o método `filter()` e `order_by()` para aplicar filtros e ordenações.

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from exercicios_sqlalchemy_01 import Funcionario


engine = create_engine('sqlite:///data/empresa.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

funcionarios = session.query(Funcionario).filter(Funcionario.salario > 50000).order_by(Funcionario.data_admissao.desc()).all()

for funcionario in funcionarios:
    print(funcionario.id, funcionario.nome, funcionario.cargo, funcionario.data_admissao, funcionario.salario)
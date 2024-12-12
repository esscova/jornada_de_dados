"""
Consultas Complexas com `join`

Objetivo: Realizar consultas mais complexas com o uso de `join`.

Tarefa:

- Adicione uma nova tabela chamada `departamentos` com as colunas:
    - `id`: inteiro (chave primária).
    - `nome`: texto.

- Relacione cada funcionário a um departamento com uma chave estrangeira
 (campo `departamento_id` na tabela `funcionarios`).

- Faça uma consulta que retorne todos os funcionários junto com o nome do departamento 
  onde trabalham.

Dicas:

- Use a função `join()` para realizar o relacionamento entre as duas tabelas.
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


# conexao com bd
engine = create_engine('sqlite:///data/empresa2.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# classe Base Departamento
class Departamento(Base):
    __tablename__ = 'departamentos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)

    funcionarios = relationship("Funcionario", back_populates="departamento") # relacionamento com funcionarios

# classe Base Funcionario
class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cargo = Column(String)
    data_admissao = Column(String)
    salario = Column(Integer)
    departamento_id = Column(Integer, ForeignKey('departamentos.id'))  # FK

    departamento = relationship("Departamento", back_populates="funcionarios") # relacionamento com departamento

# criando as tabelas no bd
Base.metadata.create_all(engine)

# populando tabelas
session.add_all([
    Departamento(id=1, nome='RH'),
    Departamento(id=2, nome='TI'),
    Departamento(id=3, nome='Vendas'),
    Departamento(id=4, nome='Marketing'),
    Departamento(id=5, nome='Financeiro')
])

session.add_all([
    Funcionario(id=1, nome='Alice', cargo='Gerente', data_admissao='2015-01-01', salario=50000, departamento_id=1),
    Funcionario(id=2, nome='Bob', cargo='Analista', data_admissao='2016-02-15', salario=40000, departamento_id=2),
    Funcionario(id=3, nome='Charlie', cargo='Coordenador', data_admissao='2017-03-10', salario=30000, departamento_id=3),
    Funcionario(id=4, nome='David', cargo='Assistente', data_admissao='2020-05-20', salario=25000, departamento_id=4),
    Funcionario(id=5, nome='Eva', cargo='Diretora', data_admissao='2018-09-05', salario=75000, departamento_id=5)
])

session.commit()

#consulta com join
result = session.query(Funcionario, Departamento.nome).join(Departamento).all()

for funcionario, departamento_nome in result:
    print(f'{funcionario.nome} trabalha no departamento de {departamento_nome}')

session.commit()


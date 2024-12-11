#########################
# EXERCÍCIOS SQLALCHEMY #
#########################

# pacotes
from faker import Faker
from sqlalchemy import func
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Index, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
from pathlib import Path
import random

# configs
BD_URL = Path("data")/"exercicios_sqlalchemy.db"
faker = Faker()
Base = declarative_base()
engine = create_engine(f"sqlite:///{BD_URL}")
Session = sessionmaker(bind=engine)
session = Session()

# tabelas
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    vip = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    pedidos = relationship("Pedido", back_populates="usuario")

    __table_args__ = (Index('idx_email', email, unique=True),)

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    valor = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    usuario = relationship("Usuario", back_populates="pedidos")

    __table_args__ = (Index('idx_data_pedido', created_at),)


# funcoes para interagir com o banco de dados
def criar_banco_dados():
    Base.metadata.create_all(engine)

def popular_banco_dados():
    for _ in range(100):
        usuario = Usuario(
            nome=faker.name(),
            email=faker.email(),
            created_at = faker.date_time_between(start_date="-2y", end_date="now"),
        )
        session.add(usuario)
        session.commit()

    for _ in range(200):
        pedido = Pedido(
            usuario_id=random.randint(1, 100),
            valor=random.randint(1, 12000),
            created_at=faker.date_time_between(start_date="-2y", end_date="now"),
        )

        session.add(pedido)
        session.commit()

    session.close()

def criar_e_popular_banco_dados():
    criar_banco_dados()
    popular_banco_dados()

# funções para interagir com o usuario
def listar_usuarios():
    usuarios = session.query(Usuario).all()
    return usuarios

def listar_pedidos():
    pedidos = session.query(Pedido).all()
    return pedidos

def consulta_agregadas():
    '''
    Liste todos os usuários que fizeram pedidos com valor total acima de $5000.
    Gere o total gasto por cada usuário e ordene os resultados por valor gasto.
    '''
    usuarios = (
        session.query(Usuario.nome, func.sum(Pedido.valor).label('total_gasto'))
        .join(Pedido, Pedido.usuario_id == Usuario.id)
        .group_by(Usuario.id)
        .having(func.sum(Pedido.valor) > 5000)
        .order_by(func.sum(Pedido.valor).desc())
        .all()
    )

    return usuarios

# Atualize a tabela usuarios para marcar como "VIP" aqueles que gastaram mais de $10000 em pedidos.
def atualizar_vips():
    usuarios_vip = (
        session.query(Usuario)
        .join(Pedido, Pedido.usuario_id == Usuario.id)
        .group_by(Usuario.id)
        .having(func.sum(Pedido.valor) > 10000)
        .all()
    )

    for usuario in usuarios_vip:
        usuario.vip = True

    session.commit()

# listar usuarios VIP
def listar_usuarios_vip():
    usuarios_vip = session.query(Usuario).filter(Usuario.vip == True).all()
    return usuarios_vip

# Liste os pedidos (id, valor, data_pedido) juntamente com os dados dos usuários que os fizeram (nome, email)
def listar_pedidos_com_usuarios():
    pedidos = (
        session.query(Pedido.id, Pedido.created_at, Pedido.valor, Usuario.nome, Usuario.email)
        .join(Usuario, Usuario.id == Pedido.usuario_id)
        .all()
    )
    return pedidos

# funcao principal
def main():

    while True:
        print('\nEXERCÍCIOS SQLALCHEMY')
        print('1 - Criar e Popular Banco de Dados com Faker')
        print('2 - Listar Usuários')
        print('3 - Listar Pedidos')
        print('4 - Consulta Agregada: Listar Usuários com Pedidos > 5000')
        print('5 - Atualizar Vips')
        print('6 - Listar Usuários VIP')
        print('7 - Listar Pedidos com Usuarios')
        print('11 - Sair')
        opcao = input('\nEscolha uma opção: ')

        match opcao:
            case '1':
                criar_e_popular_banco_dados()
                
            case '2':
                for usuario in listar_usuarios():
                    print(f'ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}, Criado em: {usuario.created_at}')
            
            case '3':
                for pedido in listar_pedidos():
                    print(f'ID: {pedido.id}, Usuario ID: {pedido.usuario_id}, Valor: {pedido.valor}, Criado em: {pedido.created_at}')
            
            case '4':
                for usuario in consulta_agregadas():
                    print(f'Nome: {usuario[0]}, Total Gasto: {usuario[1]}')             
            
            case '5':
                atualizar_vips()
            
            case '6':
                for usuario in listar_usuarios_vip():
                    print(f'ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}, Criado em: {usuario.created_at}')
            case '7':
                for pedido in listar_pedidos_com_usuarios():
                    print(f'ID: {pedido.id}, Data do Pedido: {pedido.created_at}, Valor: {pedido.valor}, Nome do Usuário: {pedido.nome}, Email do Usuário: {pedido.email}')
            case '11':
                print('Encerrando o sistema...')
                break

if __name__ == "__main__":
    main()
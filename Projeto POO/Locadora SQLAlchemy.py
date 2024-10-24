from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

engine = create_engine('sqlite:///biblioteca.db')
Session = sessionmaker(bind=engine)
session = Session()

# Criar a base declarativa
Base = declarative_base()

# Classe Cliente (agora com SQLAlchemy)
class Cliente(Base):
    __tablename__ = 'clientes'

    cpf = Column(String(11), primary_key=True)  # CPF como chave primária
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    contato = Column(String, nullable=False)
    endereco = Column(String, nullable=False)

    alugueis = relationship("Aluguel", back_populates="cliente")

# Classe Diretor
class Diretor(Base):
    __tablename__ = 'diretores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_diretor = Column(String, nullable=False)

    filmes = relationship("Filme", back_populates="diretor")

# Classe Produtora
class Produtora(Base):
    __tablename__ = 'produtoras'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_produtora = Column(String, nullable=False)

    filmes = relationship("Filme", back_populates="produtora")

# Classe Filme
class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_filme = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    ano_estreia = Column(Integer, nullable=False)
    classificacao = Column(String, nullable=False)
    sinopse = Column(String, nullable=True)

    diretor_id = Column(Integer, ForeignKey('diretores.id'), nullable=False)
    produtora_id = Column(Integer, ForeignKey('produtoras.id'), nullable=False)

    diretor = relationship("Diretor", back_populates="filmes")
    produtora = relationship("Produtora", back_populates="filmes")

    alugueis = relationship("Aluguel", back_populates="filme")

# Classe Aluguel
class Aluguel(Base):
    __tablename__ = 'alugueis'

    id = Column(Integer, primary_key=True, autoincrement=True)
    preco = Column(Float, nullable=False)
    tempo_aluguel = Column(Integer, nullable=False)
    data_aluguel = Column(DateTime, default=datetime.now)

    cliente_cpf = Column(String, ForeignKey('clientes.cpf'), nullable=False)
    filme_id = Column(Integer, ForeignKey('filmes.id'), nullable=False)

    cliente = relationship("Cliente", back_populates="alugueis")
    filme = relationship("Filme", back_populates="alugueis")

Base.metadata.create_all(engine)


def cadastrar_diretor(nome):
    diretor = session.query(Diretor).filter_by(nome_diretor = nome).first()
    if not diretor:
        diretor = Diretor(nome_diretor = nome)
        session.add(diretor)
        session.commit()

def cadastrar_produtora(nome):
    produtora = session.query(Produtora).filter_by(nome_produtora = nome).first()
    if not produtora:
        produtora = Produtora(nome_produtora = nome)
        session.add(produtora)
        session.commit()

def cadastrar_cliente(cpf, nome, idade, contato, endereco):
    cliente = session.query(Cliente).filter_by(cpf = cpf).first()
    if not cliente:
        cliente = Cliente(cpf = cpf, nome = nome, idade = idade, contato = contato, endereco = endereco)
        session.add(cliente)
        session.commit()

def cadastrar_filme(nome_filme, genero, ano_estreia, classificacao, sinopse, diretor, produtora):
    produtora = session.query(Produtora).filter_by(nome_produtora = produtora).first()
    diretor = session.query(Diretor).filter_by(nome_diretor = diretor).first()

    if produtora and diretor:
        filme = Filme(nome_filme = nome_filme, genero = genero, ano_estreia = ano_estreia,
                     classificacao = classificacao, sinopse = sinopse, diretor = diretor, produtora = produtora)
        session.add(filme)
        session.commit()
    else:
        print("Produtora ou Diretor não encontrado")




from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base
import sys
import os
# from Locadora import main

Base = declarative_base()

engine = create_engine('sqlite:///Locadora.db')

Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

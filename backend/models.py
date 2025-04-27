from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Time(Base):
    __tablename__ = 'times'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    jogo_principal = Column(String, nullable=False)

    jogadores = relationship("Jogador", back_populates="time")

class Jogador(Base):
    __tablename__ = 'jogadores'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    posicao = Column(String, nullable=True)
    time_id = Column(Integer, ForeignKey('times.id'))

    time = relationship("Time", back_populates="jogadores")

# Criação do banco de dados
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# Sessão para manipular o banco
Session = sessionmaker(bind=engine)

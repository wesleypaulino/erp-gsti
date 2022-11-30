from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base


class Tecnicos(Base):
    __tablename__ = 'tecnicos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    status = Column(String)


class Patrimonio(Base):
    __tablename__ = 'patrimonio'

    id = Column(Integer, primary_key=True, index=True)
    patrimonio = Column(String)
    depto = Column(String)
    serivcetag = Column(String)
    garantia = Column(String)
    status = Column(String)


class Licenca(Base):
    __tablename__ = 'licencas'

    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String)
    chave = Column(String)
    nota = Column(String)
    solcompra = Column(String)
    pedcompra = Column(String)

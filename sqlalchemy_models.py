# coding: utf-8
from sqlalchemy import Column, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ResumenAmigos(Base):
    __tablename__ = 'resumen_amigos'

    id = Column(INTEGER(11), primary_key=True)
    json = Column(Text)
import os

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_all():
    Base.metadata.create_all(engine)


def drop_all():
    Base.metadata.drop_all(engine)


class Document(Base):
    __tablename__ = "documents"
    id = Column(String, primary_key=True)
    description = Column(String)


class Search(Base):
    __tablename__ = "searches"
    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    document_id = Column(String, ForeignKey("documents.id"))


# Create the database engine (replace the DATABASE_URL with your actual database URL)
DATABASE_URL = "postgresql://postgres:postgres@database:5432/similarity_search_db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

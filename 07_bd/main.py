from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "pessoa"
    id = Column("pessoa_id", Integer, primary_key=True)
    name = Column("nome", String)
    city = Column("cidade", String)

    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

    def __repr__(self):
        return f"({self.id} • {self.name}, {self.city})"

engine = create_engine("sqlite:///fiap-alunos.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# conn = engine.connect()
# conn.execute("CREATE TABLE pessoa(pessoa_id INTEGER PRIMARY_KEY, nome text, cidade text);")

# CREATE OBJECTS
# person = Person(2, "Olívia", "Loures")
# session.add(person)
# session.commit()

results = session.query(Person).all()
print(results)

######------######

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import Session

# Base = declarative_base()

# def testar_conexao():
#     session = Session()

# class Curso(Base):
#     id = sqlalchemy.Column(sqlalchemy.INT)

# def print_hi(name):
#     print(f'Hi, :{name}')

# if __name__== '__main__':
#     print_hi('PyCharm')

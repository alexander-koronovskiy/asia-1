from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Подключение к базе данных
engine = create_engine('sqlite:///shop.db', echo=True)
Base = declarative_base()

# Создание таблицы
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()


# Определение структуры таблицы
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)

# Добавление нового товара
def add_item(name, description, price: float):
    new_product = Product(name=name, description = description, price = price)
    session.add(new_product)
    session.commit()
    session.close()

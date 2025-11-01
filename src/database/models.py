from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, BigInteger, Text


class Base(DeclarativeBase):
    pass


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    tg_user_id = Column(BigInteger)
    username = Column(String(255))
    is_subscription = Column(Boolean, default=True)

    def __str__(self):
        return f"Клиент: {self.username} | {self.tg_user_id}"



class ProductType(Base):
    __tablename__ = "products_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __str__(self):
        return f"Тип продукта: {self.name}"


class Product(Base):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    quantity = Column(Integer)
    description = Column(Text)
    subtype_id = Column(Integer, ForeignKey("ProductType.id"))

    def __str__(self):
        return f"Товар: {self.name}"

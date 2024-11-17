from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, BigInteger, DECIMAL


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


class ManufacturerCompany(Base):
    __tablename__ = "manufacturer_companies"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __str__(self):
        return f"Фирма производитель: {self.name}"


class Subtype(Base):
    __tablename__ = "Subtype"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    products_type_id = Column(Integer, ForeignKey("products_types.id"))
    manufacturer_company_id = Column(Integer, ForeignKey("manufacturer_companies.id"))

    def __str__(self):
        return f"Подтип: {self.name}"


class Product(Base):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Integer)
    quantity = Column(Integer)
    subtype_id = Column(Integer, ForeignKey("Subtype.id"))

    def __str__(self):
        return f"Товар: {self.name}"

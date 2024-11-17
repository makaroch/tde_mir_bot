from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from src.database.models import Base, Client, Product, ProductType, ManufacturerCompany, Subtype
from src.database.db_settings import create_db_url

engine = create_engine(create_db_url())

Base.metadata.create_all(bind=engine)


class DbWorker:
    def __init__(self, engine):
        self.__engine = engine

    def create_new_user_if_not_exists(self, tg_user_id: int, username: str):
        with Session(autoflush=False, bind=self.__engine) as db:
            user = db.query(Client).filter(Client.tg_user_id == tg_user_id).first()
            if not user:
                new_user = Client(tg_user_id=tg_user_id, username=username)
                db.add(new_user)
                db.commit()

    def get_all_type_product(self):
        with Session(autoflush=False, bind=self.__engine) as db:
            q = (
                select(ProductType)
                .select_from(ProductType)
                .join(Subtype, Subtype.products_type_id == ProductType.id)
                .join(Product, Product.subtype_id == Subtype.id)
                .where(Product.quantity > 0)
                .group_by(ProductType.id)
                .order_by(ProductType.name)
            )
            return db.execute(q).scalars().all()

    def get_manufacturer_by_type_product(self, products_type_id):
        with Session(autoflush=False, bind=self.__engine) as db:
            q = (
                select(ManufacturerCompany)
                .select_from(Subtype)
                .join(ManufacturerCompany, ManufacturerCompany.id == Subtype.manufacturer_company_id)
                .join(Product, Subtype.id == Product.subtype_id)
                .where(Subtype.products_type_id == products_type_id, Product.quantity > 0)
                .group_by(ManufacturerCompany.id)
                .order_by(ManufacturerCompany.name)

            )
            return db.execute(q).scalars().all()

    def get_subtype_by_manufacturer_and_type_id(self, m_id, type_id):
        with Session(autoflush=False, bind=self.__engine) as db:
            q = (
                select(Subtype)
                .select_from(Subtype)
                .join(Product, Subtype.id == Product.subtype_id)
                .where(Subtype.products_type_id == type_id, Subtype.manufacturer_company_id == m_id,
                       Product.quantity > 0)
                .group_by(Subtype.id)
                .order_by(Subtype.name)
            )
            return db.execute(q).scalars().all()

    def get_all_product_by_subtypes_id(self, subtypes_id):
        with Session(autoflush=False, bind=self.__engine) as db:
            q = (
                select(Product)
                .select_from(Product)
                .where(Product.subtype_id == subtypes_id, Product.quantity > 0)
                .order_by(Product.name)
            )
            return db.execute(q).scalars().all()

    def create_product_type_if_not_exists(self, product_type_name: str) -> int:
        with Session(autoflush=False, bind=self.__engine) as db:
            product_type = db.query(ProductType).filter(ProductType.name == product_type_name.title()).first()
            if not product_type:
                product_type = ProductType(name=product_type_name.title())
                db.add(product_type)
                db.commit()
            return product_type.id

    def create_manufacturer_company_if_not_exists(self, manufacturer_company_name: str) -> int:
        with Session(autoflush=False, bind=self.__engine) as db:
            manufacturer_company = db.query(ManufacturerCompany).filter(
                ManufacturerCompany.name == manufacturer_company_name.title()).first()
            if not manufacturer_company:
                manufacturer_company = ManufacturerCompany(name=manufacturer_company_name.title())
                db.add(manufacturer_company)
                db.commit()
            return manufacturer_company.id

    def create_subtype_if_not_exists(self, subtype_name: str, type_id: int, man_id: int) -> int:
        with Session(autoflush=False, bind=self.__engine) as db:
            obj = db.query(Subtype).filter(Subtype.name == subtype_name, Subtype.products_type_id == type_id,
                                           Subtype.manufacturer_company_id == man_id).first()
            if not obj:
                obj = Subtype(
                    name=subtype_name,
                    products_type_id=type_id,
                    manufacturer_company_id=man_id,
                )
                db.add(obj)
                db.commit()
            return obj.id

    def save_product(self, name: str, price: int, subtype_id: int, quantity: int):
        with Session(autoflush=False, bind=self.__engine) as db:
            product = db.query(Product).filter(Product.name == name, Product.subtype_id == subtype_id).first()
            if product:
                product.quantity = quantity
                product.price = price
            else:
                product = Product(
                    name=name,
                    price=price,
                    subtype_id=subtype_id,
                    quantity=quantity
                )
            db.add(product)
            db.commit()


DB = DbWorker(engine=engine)

from sqlalchemy import (
    Column,
    String,
    Enum,
    Boolean,
    Integer,
    CheckConstraint,
    SmallInteger,
    Table,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from models import ProductClassification, Platform as PlatformModel

Base = declarative_base()


def get_enum_values(enum) -> list[str]:
    return [str(e.value) for e in enum]


platform_and_product_association_table = Table(
    'platform_and_product_association', Base.metadata,
    Column('product_id', ForeignKey('products.id')),
    Column('platform_id', ForeignKey('platforms.id'))
)


class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(
        Enum(PlatformModel, create_constraint=True, values_callable=get_enum_values),
        nullable=False,
    )


class Product(Base):
    __tablename__ = "products"

    id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    np_title_id = Column(String(12), unique=True, nullable=False)
    classification = Column(
        Enum(ProductClassification, create_constraint=True, values_callable=get_enum_values),
        nullable=False,
    )

    # todo подумать, что использовать в качестве картинки и как хранить
    logo_url = Column(String(), nullable=True)
    is_preorder = Column(Boolean(), nullable=False)

    # todo подумать, вынести ли инфо о цене в отдельную таблицу
    base_price_in_rubles = Column(Integer(), nullable=False)
    discounted_price_in_rubles = Column(Integer(), nullable=False)
    discount_percentage = Column(SmallInteger(), nullable=False)

    platforms = relationship(
        "Platform",
        secondary=platform_and_product_association_table,
    )

    __table_args__ = (
        CheckConstraint("base_price_in_rubles >= 0", name="positive_base_price_in_rubles_constraint"),
        CheckConstraint("discounted_price_in_rubles >= 0", name="positive_discounted_price_in_rubles_constraint"),
    )

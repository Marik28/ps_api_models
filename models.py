import enum

from pydantic import BaseModel, Field


class ProductClassification(str, enum.Enum):
    FULL_GAME = "Полная версия игры"
    PREMIUM_EDITION = "Премиум-издание"
    DEMO_VERSION = "Демо-версия"


class MediaType(str, enum.Enum):
    VIDEO = "VIDEO"
    IMAGE = "IMAGE"


class Media(BaseModel):
    typename: str = Field(..., alias="__typename")
    type: MediaType
    url: str
    role: str


class Price(BaseModel):
    typename: str = Field(..., alias="__typename")
    base_price: str = Field(..., alias="basePrice")
    discounted_price: str = Field(..., alias="discountedPrice")


class Product(BaseModel):
    name: str
    platforms: list[str]
    typename: str = Field(..., alias="__typename")
    id: str
    localized_store_display_classification: ProductClassification = Field(
        ...,
        alias="localizedStoreDisplayClassification"
    )
    media: list[Media]
    price: Price


class CategoryGridRetrieve(BaseModel):
    products: list[Product]


class Data(BaseModel):
    category_grid_retrieve: CategoryGridRetrieve = Field(..., alias="categoryGridRetrieve")


class ApiResponse(BaseModel):
    data: Data

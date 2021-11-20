import enum
from typing import Optional

from pydantic import BaseModel, Field


class UpsellServiceBranding(str, enum.Enum):
    PS_PLUS = "PS_PLUS"
    EA_ACCESS = "EA_ACCESS"


class Typename(str, enum.Enum):
    SKU_PRICE = "SkuPrice"
    SKU = "Sku"
    MEDIA = "Media"
    PRODUCT = "Product"
    PAGE_INFO = "PageInfo"
    CATEGORY_GRID = "CategoryGrid"


class ProductClassification(str, enum.Enum):
    FULL_GAME = "Полная версия игры"
    PREMIUM_EDITION = "Премиум-издание"
    GAME_BUNDLE = "Игровой комплект"
    ADDON_PACK = "Пакет дополнений"
    LEVEL = "Уровень"
    GAME_APPLICATION = "Игровое приложение"
    DEMO = "Демо-версия"
    OTHER = "Дополнение"
    SOUNDTRACK = "Звуковое сопровождение"
    BUNDLE = "Комплект"


class MediaRole(str, enum.Enum):
    BACKGROUND = 'BACKGROUND'
    EDITION_KEY_ART = 'EDITION_KEY_ART'
    FOUR_BY_THREE_BANNER = 'FOUR_BY_THREE_BANNER'
    GAME_HUB_COVER_ART = 'GAMEHUB_COVER_ART'
    LOGO = 'LOGO'
    MASTER = 'MASTER'
    PORTRAIT_BANNER = 'PORTRAIT_BANNER'
    PREVIEW = 'PREVIEW'
    SCREENSHOT = 'SCREENSHOT'


class MediaType(str, enum.Enum):
    VIDEO = "VIDEO"
    IMAGE = "IMAGE"


class PageInfo(BaseModel):
    typename: Typename = Field(..., alias="__typename")
    is_last: bool = Field(..., alias="isLast")
    total_count: int = Field(..., alias="totalCount")

    class Config:
        allow_population_by_field_name = True


class Media(BaseModel):
    typename: Typename = Field(..., alias="__typename")
    type: MediaType
    url: str
    role: MediaRole

    class Config:
        allow_population_by_field_name = True


class Price(BaseModel):
    typename: Typename = Field(..., alias="__typename")
    base_price: str = Field(..., alias="basePrice")
    discounted_price: str = Field(..., alias="discountedPrice")
    is_free: bool = Field(..., alias="isFree")
    is_tied_to_subscription: Optional[bool] = Field(None, alias="isTiedToSubscription")
    is_exclusive: bool = Field(..., alias="isExclusive")
    discount_text: Optional[str] = Field(None, alias="discountText")
    service_branding: Optional[list] = Field(..., alias="serviceBranding")
    upsell_service_branding: Optional[list[UpsellServiceBranding]] = Field(..., alias="upsellServiceBranding")
    upsell_text: Optional[str] = Field(..., alias="upsellText")

    class Config:
        allow_population_by_field_name = True


class Platform(str, enum.Enum):
    PS4 = "PS4"
    PS5 = "PS5"


class SkuType(str, enum.Enum):
    STANDARD = "STANDARD"
    PREORDER = "PREORDER"


class Skus(BaseModel):
    typename: Typename = Field(..., alias="__typename")
    type: SkuType

    class Config:
        allow_population_by_field_name = True


class Product(BaseModel):
    name: str
    platforms: list[Platform]
    typename: Typename = Field(..., alias="__typename")
    id: str
    np_title_id: str = Field(..., alias="npTitleId")
    localized_store_display_classification: ProductClassification = Field(
        ...,
        alias="localizedStoreDisplayClassification"
    )
    media: list[Media]
    price: Optional[Price]
    skus: list[Skus]

    class Config:
        allow_population_by_field_name = True


class CategoryGridRetrieve(BaseModel):
    products: list[Product]
    typename: Typename = Field(..., alias="__typename")
    id: str
    reporting_name: str = Field(..., alias="reportingName")
    page_info: PageInfo = Field(..., alias="pageInfo")

    class Config:
        allow_population_by_field_name = True


class Data(BaseModel):
    category_grid_retrieve: CategoryGridRetrieve = Field(..., alias="categoryGridRetrieve")

    class Config:
        allow_population_by_field_name = True


class ApiResponse(BaseModel):
    data: Data

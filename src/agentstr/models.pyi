from logging import Logger
from typing import ClassVar, List, Set

from nostr_sdk import (
    Keys,
    Metadata,
    ProductData,
    PublicKey,
    ShippingCost,
    ShippingMethod,
    StallData,
)
from pydantic import BaseModel

class Profile:
    """
    Generic Profile class that holds the metadata of a Nostr profile.
    """

    logger: ClassVar[Logger]
    about: str
    banner: str
    display_name: str
    name: str
    picture: str
    website: str

    def __init__(self) -> None: ...
    def get_about(self) -> str: ...
    def get_banner(self) -> str: ...
    def get_display_name(self) -> str: ...
    def get_name(self) -> str: ...
    def get_picture(self) -> str: ...
    def get_website(self) -> str: ...
    def set_about(self, about: str) -> None: ...
    def set_banner(self, banner: str) -> None: ...
    def set_display_name(self, display_name: str) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_picture(self, picture: str) -> None: ...
    def set_website(self, website: str) -> None: ...
    def to_json(self) -> str: ...

class AgentProfile(Profile):
    PROFILE_URL_PREFIX: ClassVar[str]
    profile_url: str
    keys: Keys

    def __init__(self, keys: Keys) -> None: ...
    @classmethod
    def from_metadata(cls, metadata: Metadata, keys: Keys) -> "AgentProfile": ...
    def get_private_key(self) -> str: ...
    def get_public_key(self) -> str: ...
    def to_json(self) -> str: ...

class NostrProfile(Profile):
    public_key: PublicKey
    profile_url: str
    PROFILE_URL_PREFIX: ClassVar[str]
    locations: Set[str]

    def __init__(self, public_key: PublicKey) -> None: ...
    @classmethod
    def from_metadata(
        cls, metadata: Metadata, public_key: PublicKey
    ) -> "NostrProfile": ...
    def add_location(self, location: str) -> None: ...
    def get_public_key(self) -> str: ...
    def get_locations(self) -> Set[str]: ...
    def get_profile_url(self) -> str: ...
    def get_zip_codes(self) -> List[str]: ...
    def to_json(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class MerchantProduct(BaseModel):
    id: str
    stall_id: str
    name: str
    description: str
    images: List[str]
    currency: str
    price: float
    quantity: int
    shipping: List[ShippingCost]
    categories: List[str]
    specs: List[List[str]]

    @classmethod
    def from_product_data(cls, product_data: ProductData) -> "MerchantProduct": ...
    def to_product_data(self) -> ProductData: ...
    def to_dict(self) -> dict: ...

class MerchantStall(BaseModel):
    id: str
    name: str
    description: str
    currency: str
    shipping: List[ShippingMethod]
    geohash: str

    @classmethod
    def from_stall_data(cls, stall_data: StallData) -> "MerchantStall": ...
    def get_geohash(self) -> str: ...
    def set_geohash(self, geohash: str) -> None: ...
    def to_dict(self) -> dict: ...
    def to_stall_data(self) -> StallData: ...

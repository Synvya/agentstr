from typing import List

from agno.tools import Toolkit
from synvya_sdk import NostrClient, Product, Profile, Stall

class SellerTools(Toolkit):
    _nostr_client: NostrClient
    _profile: Profile
    _stalls: List[Stall]
    _products: List[Product]

    def __init__(
        self,
        relay: str,
        private_key: str,
        stalls: List[Stall],
        products: List[Product],
    ) -> None: ...
    def get_profile(self) -> str: ...
    def get_relay(self) -> str: ...
    def get_products(self) -> str: ...
    def get_stalls(self) -> str: ...
    def publish_all_products(self) -> str: ...
    def publish_all_stalls(self) -> str: ...
    def publish_new_product(self, product: Product) -> str: ...
    def publish_product_by_name(self, product_name: str) -> str: ...
    def publish_products_by_stall_name(self, stall_name: str) -> str: ...
    def publish_profile(self) -> str: ...
    def publish_new_stall(self, stall: Stall) -> str: ...
    def publish_stall_by_name(self, stall_name: str) -> str: ...
    def remove_all_products(self) -> str: ...
    def remove_all_stalls(self) -> str: ...
    def remove_product_by_name(self, product_name: str) -> str: ...
    def remove_stall_by_name(self, stall_name: str) -> str: ...

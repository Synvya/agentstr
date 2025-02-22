from logging import Logger
from typing import ClassVar

from agno.agent import AgentKnowledge
from agno.tools import Toolkit

from agentstr.models import AgentProfile, NostrProfile
from agentstr.nostr import NostrClient

class BuyerTools(Toolkit):
    logger: ClassVar[Logger]
    sellers: set[NostrProfile]
    relay: str
    _nostr_client: NostrClient

    def __init__(
        self, knowledge_base: AgentKnowledge, buyer_profile: AgentProfile, relay: str
    ) -> None: ...
    def find_seller_by_name(self, name: str) -> str: ...
    def find_seller_by_public_key(self, public_key: str) -> str: ...
    def find_sellers_by_location(self, location: str) -> str: ...
    def get_nostr_client(self) -> NostrClient: ...
    def get_profile(self) -> str: ...
    def get_relay(self) -> str: ...
    def get_seller_stalls(self, public_key: str) -> str: ...
    def get_seller_count(self) -> str: ...
    def get_seller_products(self, public_key: str) -> str: ...
    def get_sellers(self) -> str: ...
    def purchase_product(self, product: str) -> str: ...
    def refresh_sellers(self) -> str: ...
    def _refresh_sellers(self) -> None: ...
    def _store_response_in_knowledge_base(self, response: str) -> None: ...

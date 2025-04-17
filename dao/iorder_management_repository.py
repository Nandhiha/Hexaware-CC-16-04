from abc import ABC, abstractmethod
from typing import List
from entity.users import Users
from entity.products import Products
from entity.order import Order

class IOrderManagementRepository(ABC):

    @abstractmethod
    def create_user(self, user: Users) -> None:
        """Creates a new user in the database"""
        pass

    @abstractmethod
    def create_product(self, user: Users, product: Products) -> None:
        """Creates a new product (admin only)"""
        pass

    @abstractmethod
    def create_order(self, user: Users, products: List[Products]) -> None:
        """Creates an order for the given user and products"""
        pass

    @abstractmethod
    def cancel_order(self, user_id: int, order_id: int) -> None:
        """Cancels an existing order if it belongs to the given user"""
        pass

    @abstractmethod
    def get_all_products(self) -> List[Products]:
        """Returns a list of all products"""
        pass

    @abstractmethod
    def get_orders_by_user(self, user: Users) -> List[Order]:
        """Returns all orders placed by the specified user"""
        pass

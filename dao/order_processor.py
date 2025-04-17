# dao/order_processor.py
from abc import ABC, abstractmethod
from entity.users import Users  # Corrected import to use the 'Users' class
from entity.order import Order

class OrderProcessor(ABC):

    @abstractmethod
    def get_orders_by_user(self, user):
        pass

    @abstractmethod
    def create_user(self, user: Users):
        pass

    @abstractmethod
    def create_product(self, admin_user, product):
        pass

    @abstractmethod
    def create_order(self, order: Order):
        pass

    @abstractmethod
    def cancel_order(self, user_id, order_id):
        pass

    @abstractmethod
    def get_all_products(self):
        pass


# Concrete implementation of OrderProcessor
class ConcreteOrderProcessor(OrderProcessor):
    def get_orders_by_user(self, user):
        # Example implementation of the abstract method
        # You can query the database to get orders by the user.
        # For now, I'm just returning a dummy list of orders
        orders = [
            {"order_id": 1, "user_id": user.user_id, "status": "shipped"},
            {"order_id": 2, "user_id": user.user_id, "status": "pending"}
        ]
        return orders

    def create_user(self, user):
        # Implement logic to create a user
        print(f"User {user.username} created.")

    def create_product(self, admin_user, product):
        # Implement logic to create a product
        print(f"Product {product.name} created by admin {admin_user.username}.")

    def create_order(self, order):
        # Implement logic to create an order
        print(f"Order {order.order_id} created for user {order.user.username}.")

    def cancel_order(self, user_id, order_id):
        # Implement logic to cancel an order
        print(f"Order {order_id} cancelled for user {user_id}.")

    def get_all_products(self):
        # Implement logic to fetch all products
        return [{"product_id": 1, "name": "Laptop", "price": 1000}, {"product_id": 2, "name": "Shirt", "price": 25}]

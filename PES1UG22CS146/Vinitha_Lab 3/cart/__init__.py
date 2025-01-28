import json
from products import Product, get_product
from cart import dao


class Cart:
    def _init_(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list[Product]:
    """Fetches the cart contents for a given user."""
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    # Combine parsing and fetching products in a single loop
    items = [
        get_product(item)
        for cart_detail in cart_details
        for item in eval(cart_detail['contents'])
    ]
    return items


def add_to_cart(username: str, product_id: int):
    """Adds a product to the user's cart."""
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    """Removes a product from the user's cart."""
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    """Deletes the user's entire cart."""
    dao.delete_cart(username)

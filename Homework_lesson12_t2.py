class Item:
    """Class representing a product item."""

    def __init__(self, name: str, price: float, description: str):
        self.price = price
        self.description = description
        self.name = name

    def __str__(self):
        return f"{self.name}: {self.description} - {self.price}"


class User:
    """Class representing a user/customer."""

    def __init__(self, name: str, surname: str, phone_number: str):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname}, phone: {self.phone_number}"


class Purchase:
    """Class representing a purchase made by a user."""

    def __init__(self, user: User):
        self.products = {}
        self.user = user

    def add_item(self, item: Item, quantity: int):
        self.products[item] = quantity

    def __str__(self):
        result = f"Purchase for {self.user}: "
        for item, quantity in self.products.items():
            result += f"{item.name} x {quantity}, "
        result += f"Total: {self.get_total()}"
        return result

    def get_total(self):
        total = 0
        for item, quantity in self.products.items():
            total += item.price * quantity
        return total
    
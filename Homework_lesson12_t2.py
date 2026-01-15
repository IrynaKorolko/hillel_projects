class Item:

    def __init__(self, name: str, price: float, description: str):
        self.price = price
        self.description = description
        self.name = name

    def __str__(self):
        return f"{self.name}: {self.description} - {self.price}"


class User:

    def __init__(self, name: str, surname: str, phone_number: str):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname}, phone: {self.numberphone}"


class Purchase:

    def __init__(self, user: User):
        self.products = {}
        self.user = user

    def add_item(self, item, quantity: int):
        self.products.append((item, quantity))
        self.products[item] = quantity

    def __str__(self):
        result = f"Purchase for {self.user}: "
        for item, quantity in self.products:
            result += f"Total: {item.price} x {quantity}"
            result += f"Total purchase amount: {self.get_total()}"
            return result

    def get_total(self):
        total = 0
        for item, quantity in self.products:
            total += item.price * quantity
        return total

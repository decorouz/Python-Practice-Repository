"""
What are solid principles:
    - Single responsibility principle: A class should do one thing and do it well.
    - Open closed principle: A software should be open to extension but not modification:
        That is you should be able to extend a class behavior without modifying it.
    - Liskov Substitution principle: Object in a program should be replaceable with instance of their subtype
    without altering the correctness of the program. In other words, a subclass should be able to replace its
    parant class without breaking the code.
    - Interface Segregation Principle: Clients shouldn't be forced to depend on methods they do not use.
    - Dependency Inversion Principle: States that high level modules should not depend on low-level module, but
    should depend on abstractions. That is you should not have to change you code with you change 
    the implementation of a module.

"""


class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for quantity, price in zip(self.quantities, self.prices):
            total += quantity * price
        return total

    def pay(self, payment_type: str, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
order.pay("debit", "0372846")

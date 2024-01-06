"""Demonstrates Liskov Substitution Principle.
Subclass should be able to replace parent class without breaking the code.
"""

from abc import ABC, abstractmethod


class Order:
    def __init__(self) -> None:
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order) -> None:
        ...


class CreditCardPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order: Order) -> None:
        print("Processing credit card payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class DebitCardPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order: Order) -> None:
        print("Processing debit card payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class FlutterwavePaymentProcessor(PaymentProcessor):
    def __init__(self, email: str) -> None:
        self.email = email

    def pay(self, order: Order) -> None:
        print("Processing debit card payment type")
        print(f"Verifying email: {self.email}")
        order.status = "paid"


if __name__ == "__main__":
    order = Order()
    order.add_item("Tractor", 10, 50)
    order.add_item("Sprayer", 2, 100)
    order.add_item("Harvester", 2, 300)

    processor = FlutterwavePaymentProcessor("hi@email.net")
    processor.pay(order)
    print(order.status)

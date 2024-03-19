"""Demonstrate Open Closed Principle.
That is a class should be open to extension but closed to modification"""

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
    def pay(self, order: Order, security_code: str) -> None:
        print("Processing Payment")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class CreditCardPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str) -> None:
        print("Processing credit card payment")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class DebitCardPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str) -> None:
        print("Processing debit card payment")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class FlutterwavePaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str) -> None:
        print("Processing Flutterwave payment")
        print(f"Verifying email: {security_code}")
        order.status = "paid"


if __name__ == "__main__":
    order = Order()
    order.add_item("Tractor", 10, 50)
    order.add_item("Sprayer", 2, 100)
    order.add_item("Harvester", 2, 300)

    processor = CreditCardPaymentProcessor()
    processor.pay(order, "2838489")
    print(order.status)

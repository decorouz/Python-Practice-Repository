"""Interface Segregation Principle.
Clients shouldn't be forced to depend on methods they do not use.
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


class SMSAuthorizer:
    def __init__(self) -> None:
        self.authenticated = False

    def verify_code(self, code: str) -> None:
        print(f"Verifying SMS code {code}")
        self.authenticated = True

    def is_authenticated(self) -> bool:
        return self.authenticated


class DebitCardPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str, authorizer: SMSAuthorizer) -> None:
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order: Order) -> None:
        if not self.authorizer.is_authenticated:
            raise Exception("Not authenticated")

        print("Processing debit card payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditCardPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order: Order) -> None:
        print("Processing credit card payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


if __name__ == "__main__":
    order = Order()
    order.add_item("Tractor", 10, 50)
    order.add_item("Sprayer", 2, 100)
    order.add_item("Harvester", 2, 300)

    authorizer = SMSAuthorizer()
    authorizer.verify_code("12345")

    processor = DebitCardPaymentProcessor("09847338", authorizer)
    processor.pay(order)
    print(order.status)

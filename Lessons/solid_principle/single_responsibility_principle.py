class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)


class PaymentProcessor:
    def pay(self, order: Order, security_code: str):
        print("Processing Payment")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


if __name__ == "__main__":
    first_order = Order()
    first_order.add_item("Tractor", 10, 50)
    first_order.add_item("Sprayer", 2, 100)
    first_order.add_item("Harvester", 2, 300)

    processor = PaymentProcessor()
    processor.pay(first_order, "2838489")
    print(first_order.status)

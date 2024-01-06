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
    order = Order()
    order.add_item("Tractor", 10, 50)
    order.add_item("Sprayer", 2, 100)
    order.add_item("Harvester", 2, 300)

    processor = PaymentProcessor()
    processor.pay(order, "2838489")
    print(order.status)

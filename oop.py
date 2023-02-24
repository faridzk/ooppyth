import csv

class item:
    pay_rate = 0.8  # The payrate after 20% discount
    all = []

    def __init__(self, name, price, quantity=0):
        # running validations to the recieved parameters
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Asssigning the attributes to self object
        self.name = name
        self.price = price 
        self.quantity = int(quantity)

        # actions to execute
        item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv','r') as f:
            reader=csv.DictReader(f)
            items= list(reader)
        for item in items:
            print(item)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item.instantiate_from_csv()


#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount

        self.total = 0

        self.items = []

        self.transactions = []

    def add_item(self, item_name, item_price, quantity=1):
        self.total += item_price * quantity

        for _ in range(quantity):
            self.items.append(item_name)

        self.transactions.append((item_name, item_price, quantity))

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount

            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            last_item, last_price, last_quantity = self.transactions.pop()

            self.total -= last_price * last_quantity

            for _ in range(last_quantity):
                if self.items:
                    self.items.pop()

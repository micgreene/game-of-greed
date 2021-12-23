


class Banker:
    def __init__(self, shelved=0, balance=0):
        self.shelved = shelved
        self.balance = balance

    def shelf(self, points):
        self.shelved += points

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0

    def clear_shelf(self):
        self.shelved = 0
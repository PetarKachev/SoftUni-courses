class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size            # Size of the cup
        self.quantity = quantity    # How much liquid it currently holds

    def fill(self, amount):
        if self.quantity + amount < self.size:
            self.quantity += amount

    def status(self):
        result = self.size - self.quantity
        return result
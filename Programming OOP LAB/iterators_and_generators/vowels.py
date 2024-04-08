class vowels:
    def __init__(self, string: str):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.index = -1
        self.vowels_values = [c for c in self.string if c.lower() in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_values):
            return self.vowels_values[self.index]
        raise StopIteration
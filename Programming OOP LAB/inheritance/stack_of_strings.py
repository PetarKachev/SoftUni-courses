class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    def __str__(self):
        self.data = sorted(self.data, reverse=True)
        info = ', '.join(self.data)
        return f'[{info}]'
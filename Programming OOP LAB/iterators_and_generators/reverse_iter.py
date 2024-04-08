class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.start_idx = 0
        self.end_idx = len(self.iter_obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.end_idx > self.start_idx:
            self.end_idx -= 1
            return self.iter_obj[self.end_idx]
        raise StopIteration
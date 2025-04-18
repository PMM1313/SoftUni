class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.count:
            value = self.index * self.step
            self.index += 1
            return value

        raise StopIteration
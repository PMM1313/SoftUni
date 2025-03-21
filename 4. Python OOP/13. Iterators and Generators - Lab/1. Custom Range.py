class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.temp = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.temp += 1
        if self.temp > self.end:
            raise StopIteration
        return self.temp
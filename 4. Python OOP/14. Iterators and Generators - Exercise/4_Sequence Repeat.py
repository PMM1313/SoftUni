class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.number:
            i = self.index % len(self.sequence)
            self.index += 1
            return self.sequence[i]
        raise StopIteration()

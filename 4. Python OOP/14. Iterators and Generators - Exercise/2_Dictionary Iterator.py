class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary_tuple = tuple(dictionary.items())
        # self.keys = list(dictionary.keys())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.dictionary_tuple):
            i = self.current_index
            self.current_index += 1
            return self.dictionary_tuple[i]
        raise StopIteration()


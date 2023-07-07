class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = list(dictionary.items())
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):

        self.counter += 1

        if self.counter == len(self.dictionary):
            raise StopIteration

        return tuple(self.dictionary[self.counter])


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)


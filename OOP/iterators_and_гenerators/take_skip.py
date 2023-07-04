class take_skip:
    def __init__(self, step: int, count:int):
        self.step = step
        self.count = count
        self.num = 0 - self.step
        self.curr_counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_counter > self.count:
            raise StopIteration

        self.num += self.step
        self.curr_counter += 1

        return self.num


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

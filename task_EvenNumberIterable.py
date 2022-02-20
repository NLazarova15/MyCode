class EvensRange:
    """Simplest Number Iterator, which can iterate on only even numbers"""

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.curr = self.start-1

    def __next__(self):
        if self.curr <= self.end-2:
            self.curr+=2
            return self.curr
        else:
            raise StopIteration
    def __iter__(self):
        return self
        

evens_range = EvensRange(1,10)

for i in evens_range:
	print(i)

class Test():
    def __init__(self, first):
        self.first = first
        print(first)
        if self.first < 4:
            Test(first + 1)
            Test(first + 1)

Test(1)
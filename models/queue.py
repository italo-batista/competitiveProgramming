

class queue:

    def __init__(self, size):
        self.array = [0] * size
        self.tail = -1
        self.head = 0
        self.elements = 0
        self.size = size

    def push(self, element):
        self.tail = (self.tail + 1) % self.size
        self.array[self.tail] = element
        self.elements += 1

    def pop(self):
        if not self.empty():
            element = self.array[self.head]
            self.elements -= 1
            self.head = (self.head + 1) % self.size
            return element

    def empty(self):
        return self.elements == 0

    def top(self):
        return self.array[self.head]

    def my_array(self):
        return self.array
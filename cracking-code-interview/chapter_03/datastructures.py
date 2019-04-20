

class StackNode:
    def __init__(self, value, min_value=None):
        self.value = value
        self.min_value = min_value

class Stack:
    def __init__(self):
        self._array = []

    def pop(self):
        return self._array.pop().value

    def push(self, item):
        new_min = item if self._is_less_than_min(item) else self.peek().min_value
        new_item = StackNode(value=item, min_value=new_min)
        self._array.append(new_item)

    def is_empty(self):
        return len(self._array) == 0

    def peek(self):
        return self._array[-1] if len(self._array) > 0 else None

    def min(self):
        return self.peek().min_value

    def _is_less_than_min(self, item):
        if self.peek() and item < self.peek().min_value:
            return True
        elif not self.peek():
            return True
        else:
            return False


class Queue:
    def __init__(self):
        self._array = []

    def remove(self):
        self._array.pop(False)

    def add(self, item):
        self._array.append(item)

    def is_empty(self):
        return len(self._array) == 0

    def peek(self):
        return self._array[0]


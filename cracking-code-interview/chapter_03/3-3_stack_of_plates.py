import sys
sys.path.append('./datastructures')
from datastructures import Stack


class SetOfStacks:

    LIMIT_PER_STACK = 2

    def __init__(self):
        self.main_stack = Stack()

    def pop(self):
        if self.is_empty():
            return None
        elif self._top_stack().is_empty():
            self.main_stack.pop()
            self.pop()

        return self._top_stack().pop()

    def push(self, item):
        if self.is_empty():
            self.main_stack.push(Stack())
        self._top_stack().push(item)

    def is_empty(self):
        return self.main_stack.is_empty()

    def peek(self):
        if self.is_empty():
            return None
        return self._top_stack().peek().value

    def _top_stack(self):
        return self.main_stack.peek().value


if __name__ == '__main__':  # tests

    stacks = SetOfStacks()

    assert stacks.peek() is None

    stacks.push(1)
    assert stacks.peek() == 1

    stacks.push(2)
    assert stacks.peek() == 2

    stacks.push(3)
    assert stacks.pop() == 3

    assert stacks.pop() == 2

    assert stacks.pop() == 1

    assert stacks.is_empty() is not None
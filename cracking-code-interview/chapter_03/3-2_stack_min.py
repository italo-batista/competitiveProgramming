import sys
sys.path.append('./datastructures')
from datastructures import Stack

if __name__ == '__main__':  # tests

    stack = Stack()

    stack.push(1)
    assert stack.min() == 1

    stack.push(2)
    assert stack.min() == 1

    stack.push(3)
    assert stack.min() == 1

    stack.push(0)
    assert stack.min() == 0

    stack.pop()
    assert stack.min() == 1

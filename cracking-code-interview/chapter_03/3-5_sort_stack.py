import sys
sys.path.append('./datastructures')
from datastructures import Stack


def sort_stack(stack):
    temp_stack = Stack()

    threshold = stack.pop()
    while not stack.is_empty():
        if stack.peek() >= threshold:
            stack_node = stack.pop()
            temp_stack.push(threshold)
            threshold = stack_node

        elif stack.peek() < threshold:
            temp_stack.push(threshold)
            threshold = stack.pop()
            while not temp_stack.is_empty() and threshold < temp_stack.peek():
                stack.push(temp_stack.pop())
            temp_stack.push(threshold)
            if not stack.is_empty():
                threshold = stack.pop()

    temp_stack.push(threshold)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack


if __name__ == '__main__':  # tests

    stack = Stack()
    original_values = [8, 3, 5, 9, 7, 2]
    for v in original_values:
        stack.push(v)

    sorted_stack = Stack()
    sorted_values = sorted(original_values, reverse=True)
    for v in sorted_values:
        sorted_stack.push(v)

    expected_sorted_stack = sort_stack(stack)
    while not expected_sorted_stack.is_empty() and not sorted_stack.is_empty():
        assert expected_sorted_stack.pop() == sorted_stack.pop()




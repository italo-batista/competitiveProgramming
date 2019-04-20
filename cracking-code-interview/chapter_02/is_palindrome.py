import sys
sys.path.append('./linkedlist')
from linkedlist import DoublyLinkedList, DoublyNode


def is_palindrome(ll):
    # type (DoublyLinkedList) -> boolean

    curr_forwards = ll.head
    curr_backwards = ll.tail
    is_palindrome = True

    while curr_forwards and curr_backwards and curr_backwards != curr_forwards and is_palindrome:
        if curr_forwards.value != curr_backwards.value:
            is_palindrome = False
        curr_forwards = curr_forwards.next
        curr_backwards = curr_backwards.prev

    return is_palindrome


if __name__ == '__main__':  # tests
    palidrome = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    palidrome_ll = DoublyLinkedList()
    for p in palidrome:
        palidrome_ll.append(DoublyNode(value=p))
    assert is_palindrome(palidrome_ll) == True

    palidrome = [1, 2, 3, 4, 4, 3, 2, 1]
    palidrome_ll = DoublyLinkedList()
    for p in palidrome:
        palidrome_ll.append(DoublyNode(value=p))
    assert is_palindrome(palidrome_ll) == True

    not_palidrome = [1, 2, 3, 4, 5, 3, 2, 1]
    not_palidrome_ll = DoublyLinkedList()
    for p in not_palidrome:
        not_palidrome_ll.append(DoublyNode(value=p))
    assert is_palindrome(not_palidrome_ll) == False

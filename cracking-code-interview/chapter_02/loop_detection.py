import sys
sys.path.append('./linkedlist')
from linkedlist import DoublyLinkedList, DoublyNode


def has_loop(ll):
    double_ref = None
    runner1 = ll.head
    runner2 = ll.head
    first_it = True
    while runner1 and runner2:
        if runner1 == runner2 and not first_it:
            double_ref = runner1
            break

        first_it = False
        runner1 = runner1.next
        runner2 = runner2.next and runner2.next.next

    return double_ref if double_ref is not None else False


if __name__ == '__main__':  # tests

    n1 = DoublyNode(value=1)
    n2 = DoublyNode(value=2)
    n3 = DoublyNode(value=3)
    n4 = DoublyNode(value=4)
    n5 = DoublyNode(value=5)
    n6 = DoublyNode(value=6)

    n1.next = n2
    n2.next = n3
    n3.next = n6
    n6.next = n4
    n4.next = n5
    n5.next = n6

    ll = DoublyLinkedList(head=n1)

    assert has_loop(ll) is not False or not None
    assert has_loop(ll) == n6



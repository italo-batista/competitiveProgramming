import sys
sys.path.append('./linkedlist')
from linkedlist import DoublyLinkedList, DoublyNode
from get_kth_to_last import get_ll_size


def delete_mid_node(node):
    node.prev.next = node.next
    node.next.prev = node.prev


if __name__ == '__main__':  # tests

    ll = DoublyLinkedList()
    dnode1 = DoublyNode(value=1)
    dnode2 = DoublyNode(value=2)
    dnode3 = DoublyNode(value=3)
    ll.append(dnode1)
    ll.append(dnode2)
    ll.append(dnode3)
    assert get_ll_size(ll) == 3
    assert ll.head.next == dnode2

    delete_mid_node(dnode2, )
    assert get_ll_size(ll) == 2
    assert ll.head.next != dnode2

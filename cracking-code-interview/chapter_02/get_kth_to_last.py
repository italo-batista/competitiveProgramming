import sys
sys.path.append('./mcollections')
from mcollections import LinkedList, Node


def get_ll_size(ll):
    size = 0
    cnode = ll.head
    while cnode is not None:
        size += 1
        cnode = cnode.next
    return size


def solver(ll, k):
    length = get_ll_size(ll)

    i = 0
    cnode = ll.head
    while i < length - k - 1 and cnode is not None:
        cnode = cnode.next
        i += 1

    return cnode



node1 = Node(value=1)
node2 = Node(value=2)
node3 = Node(value=3)
ll = LinkedList(head=node1)
ll.append(node2)
ll.append(node3)

assert solver(ll, 1) == node2

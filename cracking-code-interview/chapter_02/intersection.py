import sys
sys.path.append('./linkedlist')
from linkedlist import LinkedList, Node

def has_intersection(ll1, ll2):
    tail1 = None
    curr_node = ll1.head
    while curr_node:
        tail1 = curr_node
        curr_node = curr_node.next

    tail2 = None
    curr_node = ll2.head
    while curr_node:
        tail2 = curr_node
        curr_node = curr_node.next

    if tail1 == tail2:
        return True

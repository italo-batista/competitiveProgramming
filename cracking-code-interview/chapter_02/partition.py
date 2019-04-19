import sys
sys.path.append('./linkedlist')
from linkedlist import DoublyLinkedList, DoublyNode, DOUBLY_NIL


def partition(ll, div_node):
    temp_ll = DoublyLinkedList()

    if ll.head is not None:
        curr_node = ll.head
    else:
        return ll

    while curr_node.value is not None:

        curr_node_next = curr_node.next
        curr_node_prev = curr_node.prev

        if curr_node.value >= div_node.value:
            temp_ll.append(DoublyNode(value=curr_node.value))

            if curr_node_prev:
                curr_node_prev.next = curr_node_next
                curr_node_next.prev = curr_node_prev

        curr_node = curr_node_next

    ll.append(temp_ll.head)
    return ll


if __name__ == '__main__':  # tests

    ll = DoublyLinkedList()
    origin_node_values = [3, 5, 8, 5, 10, 2, 1]
    partition_value = 5

    for node_value in origin_node_values:
        node = DoublyNode(value=node_value)
        ll.append(node)

    after_partition_value = False
    after_partition = partition(ll, DoublyNode(value=partition_value))

    curr_node = after_partition.head
    while curr_node.value:
        if node.value >= partition_value:
            after_partition_value = True
        if after_partition_value:
            assert node.value >= partition_value
        else:
            assert node.value < partition

        curr_node = curr_node.next

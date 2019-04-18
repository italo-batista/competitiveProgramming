

def remove_duplicates(ll):
    # type: (linked_list) -> linked_list

    freq = dict()
    node = ll.head

    while node.v != None:
        freq[node.v] = freq.get(node.v, 0) + 1

        if freq[node.v] > 1:
            node.prev.next = node.next

        node = node.next

    return ll


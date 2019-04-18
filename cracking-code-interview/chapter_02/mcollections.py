class Node(object):
    def __init__(self, next=None, value=None):
        self.next = next
        self.value = value


class DoublyNode(Node):
    def __init__(self, next=None, prev=None, value=None):
        super(DoublyNode, self).__init__(next, value)
        self.prev = prev


class LinkedList:

    def __init__(self, head=None):
        self.head = self.tail = head

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = None


class DoublyLinkedList:

    def __init__(self, head=None):
        self.head = self.tail = head

    def append(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None


# tests

dnode1 = DoublyNode(value=1)
assert dnode1.next is None
assert dnode1.prev is None
assert dnode1.value == 1

ll = DoublyLinkedList()
ll.append(dnode1)
assert ll.head.value == dnode1.value
assert ll.tail == dnode1

dnode2 = DoublyNode(value=2)
ll.append(dnode2)
assert ll.tail.value == dnode2.value
assert ll.head == dnode1
assert dnode1.next == dnode2
assert dnode2.prev == dnode1

node1 = Node(value=1)
node2 = Node(value=2)
node3 = Node(value=3)
sll = LinkedList(node1)
assert sll.head.value == 1

sll.append(node2)
sll.append(node3)
assert sll.head.next == node2
assert sll.head.next.next == node3

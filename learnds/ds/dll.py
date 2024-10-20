class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_reverse(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" ")
            current = current.prev
        print()


def get(self, index):
    current = self.head
    count = 0
    while current is not None:
        if count == index:
            return current.data
        count += 1
        current = current.next
    return None


def set(self, index, data):
    current = self.head
    count = 0
    while current is not None:
        if count == index:
            current.data = data
            return
        count += 1
        current = current.next
    return None


def reverse(self):
    if self.head is None:
        return

    current = self.head
    while current is not None:
        current.prev, current.next = current.next, current.prev
        current = current.prev


# Example usage:
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.insert_at_head(30)
dll.insert_at_tail(40)
dll.insert_at_tail(50)
dll.print_list()  # Output: 30 20 10 40 50
dll.print_reverse()  # Output: 50 40 10 20 30

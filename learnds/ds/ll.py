class Node:
    """Represents a single node in a linked list."""

    def __init__(self, data):
        """Initializes a node with the given data and no next node."""
        self.data = data
        self.next = None


class LinkedList:
    """A linked list data structure that supports various operations."""

    def __init__(self):
        """Initializes an empty linked list."""
        self.head = None
        self.tail = None

    def append(self, data):
        """Adds a new node with the specified data to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node  # Link the new node
        self.tail = new_node  # Update the tail to the new node

    def prepend(self, data):
        """Adds a new node with the specified data to the beginning of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Link the new node to the current head
            self.head = new_node  # Update the head to the new node

    def insert(self, index, data):
        """Inserts a new node with the specified data at the given index."""
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:  # Update tail if inserted at the end
            self.tail = new_node

    def delete(self, data):
        """Deletes the first node with the specified data from the list."""
        current = self.head
        if current and current.data == data:
            self.head = current.next
            if self.head is None:  # If the list becomes empty
                self.tail = None
            return
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if current is None:
            return  # Data not found
        previous.next = current.next
        if previous.next is None:  # Update tail if last node is deleted
            self.tail = previous

    def delete_at_index(self, index):
        """Deletes the node at the specified index."""
        if index == 0:
            self.head = self.head.next
            if self.head is None:  # If the list becomes empty
                self.tail = None
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current is None or current.next is None:
            raise IndexError("Index out of bounds")
        current.next = current.next.next
        if current.next is None:  # Update tail if last node is deleted
            self.tail = current

    def reverse(self):
        """Reverses the linked list in place."""
        current = self.head
        previous = None
        self.tail = current  # Update tail to the current head
        while current:
            next_node = current.next  # Store the next node
            current.next = previous  # Reverse the link
            previous = current  # Move previous to current
            current = next_node  # Move to the next node
        self.head = previous  # Update head to the new front of the list

    def print_nodes(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def set(self, index, data):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

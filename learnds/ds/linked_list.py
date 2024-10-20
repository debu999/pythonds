from pprint import pp


class Node:
    """
    Initializes a new instance of the Node class.

    Attributes:
        val: The value stored in the node.
        next: The next node in the linked list, initially set to None.
    """

    def __init__(self, val: int):
        self.val = val
        self.next: Node | None = None

    def __str__(self):
        return f"Node(val: {self.val} , next: {self.next})"

    def __repr__(self):
        return f"Node(val: {self.val} , next: {self.next})"


class LinkedList:
    """
    Initializes a new instance of the LinkedList class.
    This constructor sets the head and tail of the linked list
    to None and initializes the length to zero.

    Attributes:
        head: The first node in the linked list, initially set to None.
        tail: The last node in the linked list, initially set to None.
        length: The number of nodes in the linked list, initially set to 0.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.value = None

    def __str__(self):
        return f"LinkedList(value: {self.value} , head: {self.head} tail: {self.tail})"

    def __repr__(self):
        return f"LinkedList(value: {self.value} , head: {self.head} tail: {self.tail})"

    def print_list(self):
        """
        Prints the values of all nodes in the linked list.
        This method traverses the list starting from the head
        and outputs the value of each node until it reaches the end.
        Args:
            None
        Returns:
            None
        """
        curr = self.head
        while curr:
            print(f"Node[{curr.val}]")
            curr = curr.next

    def insert_front(self, new_data: int):
        """
        Inserts a new node at the front of the linked list.
        This method creates a new node with the provided data
        and updates the head of the list to point to this new node,
        adjusting the tail if the list was previously empty.

        Args:
            new_data: The data to be stored in the new node.

        Returns:
            None
        """

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.length += 1

    def insert_after(self, prev_node: Node | None, new_data: int):
        """
        Inserts a new node after the specified previous node.
        This method creates a new node with the provided data
        and updates the next pointer of the previous node to point to this new node.

        Args:
            prev_node: The previous node in the linked list.
            new_data: The data to be stored in the new node.

        Returns:
            None
        """
        if prev_node is None:
            print("Previous node is absent!")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        if prev_node == self.tail:
            self.tail = new_node
        self.length += 1

    def insert_after_index(self, index: int, new_data: int):
        """
        Inserts a new node after the specified index in the linked list.
        This method creates a new node with the provided data
        and updates the next pointer of the previous node to point to this new node.

        Args:
            index: The index of the previous node in the linked list.
            new_data: The data to be stored in the new node.

        Returns:
            None
        """
        prev_node = self.get_node(index)
        if prev_node is None:
            print("Previous node is absent!")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        if prev_node == self.tail:
            self.tail = new_node
        self.length += 1

    def insert_end(self, new_data: int):
        """
        Inserts a new node at the end of the linked list.
        This method creates a new node with the provided
        data and updates the tail of the list to point to this new node.

        Args:
            new_data: The data to be stored in the new node.

        Returns:
            None
        """
        n = Node(new_data)
        if not self.tail:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n
        self.length += 1

    def reverse(self):
        """
        Reverses the order of the nodes in the linked list.

        Args:
            None

        Returns:
            None
        """
        if self.head is None:
            return None
        curr = self.head
        self.tail = curr
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def delete_end(self):
        """
        Deletes the last node in the linked list.

        Args:
            None

        Returns:
            The deleted node, or None if the list is empty.
        """
        curr = self.head
        pre = None
        if not curr:
            return None
        if self.length == 1:
            self.head = self.tail = None
            self.length = 0
            return None
        while curr.next:
            pre = curr
            curr = curr.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return curr

    def delete_first(self):
        """
        Deletes the first node in the linked list.

        Args:
            None

        Returns:
            The deleted node, or None if the list is empty.
        """
        curr = self.head
        if not curr:
            return None
        if self.length == 1:
            self.head = self.tail = None
            self.length = 0
            return None
        self.head = self.head.next
        self.length -= 1
        return curr

    def delete(self, index: int):
        """
        Deletes the node at the specified index in the linked list.

        Args:
            index: The index of the node to delete.

        Returns:
            The deleted node, or None if the index is out of range.
        """
        if index == 0:
            return self.delete_first()
        if index == self.length - 1:
            return self.delete_end()
        node = self.get_node(index)
        if not node:
            return None
        curr = self.head
        while curr.next != node:
            curr = curr.next
        curr.next = node.next
        self.length -= 1
        return node

    def get_node(self, index: int):
        """
        Returns the node at the specified index in the linked list.

        Args:
            index: The index of the node to return.

        Returns:
            The node at the specified index, or None if the index is out of range.
        """
        if index < 0 or index > self.length - 1:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def set_node_value(self, index: int, val: int):
        """
        Sets the value of the node at the specified index to the provided value.

        Args:
            index: The index of the node to set the value of.
            val: The new value to set.

        Returns:
            The node at the specified index, or None if the index is out of range.
        """
        node = self.get_node(index)
        if node:
            node.val = val
        return node


if __name__ == "__main__":
    llist = LinkedList()
    pp(llist.delete_end())
    llist.insert_end(1)
    pp(llist.delete_end())
    llist.insert_end(1)
    llist.insert_end(2)
    llist.insert_end(3)
    pp(llist.delete_end())
    pp(llist.delete_end())
    llist.insert_end(2)
    llist.insert_end(3)
    llist.insert_after(llist.head.next.next, 4)
    llist.insert_end(5)
    llist.insert_front(0)
    llist.print_list()
    llist.reverse()
    llist.print_list()
    llist.delete_end()
    llist.print_list()
    pp(llist.delete_first())
    pp(llist.delete_first())
    pp(llist.delete_first())
    pp(llist.get_node(0))
    pp(llist.set_node_value(0, 45))
    pp(llist.get_node(0))
    pp(llist.set_node_value(0, 345))
    pp(llist.get_node(0))
    llist.insert_after_index(1, 3666)
    pp(
        [
            "******",
        ]
    )
    pp(llist.print_list())
    llist.delete(2)
    pp(
        [
            "******",
        ]
    )
    llist.print_list()

    def find_kth_from_end(linked_list, index):
        """
        Finds the kth node from the end of the linked list.

        Args:
            linked_list: The linked list.
            index: The node index from the end of the linked list to retrieve.

        Returns:
            The kth node from the end of the linked list, or None if the index is out of range.
        """
        slow = fast = linked_list.head
        for _ in range(index):
            if fast is None:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow

    def find_kth_from_end(linked_list: LinkedList, index: int):
        slow = fast = linked_list.head
        for _ in range(index):
            if not fast:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        return slow

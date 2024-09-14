from pprint import pp


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"Node(val: {self.val} , next: {self.next})"

    def __repr__(self):
        return f"Node(val: {self.val} , next: {self.next})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return f"LinkedList(value: {self.value} , head: {self.head} tail: {self.tail})"

    def __repr__(self):
        return f"LinkedList(value: {self.value} , head: {self.head} tail: {self.tail})"

    def print_list(self):
        curr = self.head
        while curr:
            print(f"Node[{curr.val}]")
            curr = curr.next

    def insert_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.length += 1

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Previous node is absent!")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        if prev_node == self.tail:
            self.tail = new_node
        self.length += 1

    def insert_end(self, new_data):
        n = Node(new_data)
        if not self.tail:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n
        self.length += 1

    def reverse(self):
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
        curr = self.head
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

    def get_node(self, index):
        if index < 0 or index > self.length - 1:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def set_node_value(self, index, val):
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

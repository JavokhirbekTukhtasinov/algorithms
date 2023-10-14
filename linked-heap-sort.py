class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.node = None


class linkedHeap:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove_max(self):
        if self.root is not None:
            return None

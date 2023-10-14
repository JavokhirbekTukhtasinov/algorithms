# Heap 2022.10.01 (Ryou)

from typing import Any, Callable
import math


class HeapNodeType:
    def __init__(self, data) -> None:

        self.Data = data
        self.Left = None
        self.Right = None
        self.Parent = None
        return


class LinkedHeap:
    def __init__(self, compare: Callable[[Any, Any], int]) -> None:

        if compare is None:
            raise TypeError("Null reference exception.")

        dummy = HeapNodeType(None)
        if dummy is None:
            raise MemoryError("The dynamic memory allocation failed.")
        self.Head = dummy
        # self.Head.Right = HeapNodeType(None)
        # if self.Head.Right is None: raise MemoryError ("The dynamic memory allocation failed.")
        self.Count = 0
        self.Compare = compare
        return

    def ExchangeNode(successor_node: HeapNodeType, predecessor_node: HeapNodeType, temporary_node: HeapNodeType) -> None:

        if successor_node.Left is predecessor_node:
            successor_node.Left = temporary_node
        else:
            successor_node.Right = temporary_node

        temporary_node.Left = predecessor_node.Left
        temporary_node.Right = predecessor_node.Right

        predecessor_node.Left = predecessor_node.Right = None
        return

    def Insert(self, data) -> None:

        if self.Head is None:
            raise TypeError("The linked heap is null.")

        new_node = HeapNodeType(data)
        if new_node is None:
            raise TypeError("Null reference exception.")

        new_node.Data = data
        self.Count += 1
        if self.Count <= 1:
            self.Head.Right = new_node
            new_node.Parent = self.Head.Right
            return

        successor_node = self.Head
        predecessor_node = successor_node.Right
        temporary_node = new_node

        compare = self.Compare
        count = self.Count
        pivot = 0x1 << int(math.log2(count) - 1.0)
        while pivot:
            if compare(predecessor_node.Data, temporary_node.Data) < 0:
                LinkedHeap.ExchangeNode(
                    successor_node, predecessor_node, temporary_node)
                predecessor_node, temporary_node = temporary_node, predecessor_node  # swap

            successor_node = predecessor_node
            predecessor_node = predecessor_node.Right if count & pivot else predecessor_node.Left
            pivot >>= 0x1

        if count & 0x1:
            successor_node.Right = temporary_node
        else:
            successor_node.Left = temporary_node
        return

    def RemoveNode(head_node: HeapNodeType, successor_node: HeapNodeType, predecessor_node: HeapNodeType) -> HeapNodeType:

        if successor_node.Left is predecessor_node:
            successor_node.Left = None
        else:
            successor_node.Right = None

        root_node = head_node.Right
        predecessor_node.Left = root_node.Left
        predecessor_node.Right = root_node.Right

        root_node.Left = root_node.Right = None
        head_node.Right = predecessor_node
        return root_node

    def SwapNode(successor_node: HeapNodeType, predecessor_node: HeapNodeType, child_node: HeapNodeType) -> HeapNodeType:

        if successor_node.Left is predecessor_node:
            successor_node.Left = child_node
        else:
            successor_node.Right = child_node

        direction = predecessor_node.Left is child_node
        brother_node = predecessor_node.Right if direction else predecessor_node.Left

        predecessor_node.Left = child_node.Left
        predecessor_node.Right = child_node.Right

        if direction:
            child_node.Left = predecessor_node
            child_node.Right = brother_node
        else:
            child_node.Left = brother_node
            child_node.Right = predecessor_node
        return child_node

    def Remove(self) -> Any:

        if self.Head is None:
            raise TypeError("The linked heap is null.")
        elif self.Count == 0:
            raise ValueError("The linked heap is empty.")

        if self.Count == 1:

            data = self.Head.Right.Data
            self.Head = None
            self.Count -= 1
            return data

        successor_node = self.Head
        predecessor_node = successor_node.Right  # root

        count = self.Count
        pivot = 0x1 << int(math.log2(count) - 1.0)
        while pivot:

            successor_node = predecessor_node
            predecessor_node = predecessor_node.Right if count & pivot else predecessor_node.Left
            pivot >>= 0x1

        delete_node = LinkedHeap.RemoveNode(
            self.Head, successor_node, predecessor_node)
        successor_node = self.Head
        predecessor_node = successor_node.Right  # root

        compare = self.Compare
        while predecessor_node.Left:

            child_node = predecessor_node.Left
            if predecessor_node.Right and compare(predecessor_node.Left.Data, predecessor_node.Right.Data) < 0:
                child_node = predecessor_node.Right

            if compare(predecessor_node.Data, child_node.Data) < 0:
                successor_node = LinkedHeap.SwapNode(
                    successor_node, predecessor_node, child_node)
            else:
                break

        self.Count -= 1
        data = delete_node.Data
        return data

    def DeleteNode(child_node: HeapNodeType) -> None:

        if child_node is None:
            return
        LinkedHeap.DeleteNode(child_node.Left)
        LinkedHeap.DeleteNode(child_node.Right)

        if child_node is None and child_node.Parent.Left is child_node:
            child_node.Parent.Left = None
        elif child_node is None and child_node.Parent.Right is child_node:
            child_node.Parent.Right = None
        return

    def Delete(self) -> None:

        if self.Head is None:
            return
        if self.Count != 0:
            LinkedHeap.DeleteNode(self.Head.Right)  # root
        self.Head = None
        return

    def DisplayNode(child_node: HeapNodeType, level: int, type: str) -> None:

        loop = 0
        for loop in range(0, level):
            print("   ", end="")
        if child_node is None:
            print("NULL")
            return

        print(f"-[{level}, {type}] {child_node.Data}")
        LinkedHeap.DisplayNode(child_node.Left, level + 1, "L")
        LinkedHeap.DisplayNode(child_node.Right, level + 1, "R")
        return

    def Display(self) -> None:

        if self.Head is None:
            return
        elif self.Count == 0:
            return

        LinkedHeap.DisplayNode(self.Head.Right, 0, "o")
        return


def MaxHeap(argument1: int, argument2: int) -> int: return argument1 - argument2
def MinHeap(argument1: int, argument2: int) -> int: return argument2 - argument1


array = [5, 11, 1, 15, 9, 10, 2, 7, 3, 14, 16, 4, 12, 8, 6, 13]
length = array.__len__()

# heap = LinkedHeap (MaxHeap)
heap = LinkedHeap(MinHeap)
for index in range(0, length):
    heap.Insert(array[index])
heap.Display()

for index in range(0, length):
    print(heap.Remove(), end=" ")
heap.Delete()

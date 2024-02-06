import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev

    def sorted(self) -> "LinkedList":
        sorted_list = LinkedList()

        current = self.head
        while current is not None:
            sorted_list.insert_sorted(current.data)
            current = current.next

        return sorted_list

    def insert_sorted(self, data):
        if self.head is None or data < self.head.data:
            self.insert_at_beginning(data)
            return

        current = self.head
        while current.next is not None and data > current.next.data:
            current = current.next

        self.insert_after(current, data)

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

        print()

    @staticmethod
    def merge_lists(list1: "LinkedList", list2: "LinkedList") -> "LinkedList":
        merged_list = LinkedList()
        cur1 = list1.head
        cur2 = list2.head

        while cur1 and cur2:
            if cur1.data < cur2.data:
                merged_list.insert_at_end(cur1.data)
                cur1 = cur1.next
            else:
                merged_list.insert_at_end(cur2.data)
                cur2 = cur2.next

        while cur1:
            merged_list.insert_at_end(cur1.data)
            cur1 = cur1.next

        while cur2:
            merged_list.insert_at_end(cur2.data)
            cur2 = cur2.next

        return merged_list


def get_random_linked_list(size: int) -> LinkedList:
    list = LinkedList()
    for _ in range(size):
        list.insert_at_end(random.randint(1, 100))
    return list


def main():
    list = get_random_linked_list(15)

    print("Original list:".ljust(20), end=" ")
    list.print_list()

    list.reverse_list()
    print("Reversed list:".ljust(20), end=" ")
    list.print_list()

    sorted_list = list.sorted()
    print("Sorted list:".ljust(20), end=" ")
    sorted_list.print_list()

    list_a = get_random_linked_list(10).sorted()
    list_b = get_random_linked_list(5).sorted()

    print("List A:".ljust(20), end=" ")
    list_a.print_list()

    print("List B:".ljust(20), end=" ")
    list_b.print_list()

    merged_list = LinkedList.merge_lists(list_a, list_b)
    print("Merged list (A+B):".ljust(20), end=" ")
    merged_list.print_list()


if __name__ == "__main__":
    main()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    """
    Combine the 2 input LinkedLists to provide 
    a new with only unique elements found in both

    Args:
        llist_1(class:LinkedList): the first LinkedList
        llist_2(class:LinkedList): the second LinkedList
    """
    new_items = set()
    current = llist_1.head
    while current.next is not None:
        new_items.add(current.value)
        current = current.next
    current = llist_2.head
    while current.next is not None:
        new_items.add(current.value)
        current = current.next
    final_linked_list = LinkedList()
    for i in new_items:
        final_linked_list.append(i)
    return final_linked_list


def intersection(llist_1, llist_2):
    new_items1 = set()
    new_items2 = set()
    current = llist_1.head
    while current.next is not None:
        new_items1.add(current.value)
        current = current.next
    current = llist_2.head
    while current.next is not None:
        new_items2.add(current.value)
        current = current.next
    # use python's & to get the intersection of the 2 sets
    new_items = new_items1 & new_items2
    final_linked_list = LinkedList()
    for i in new_items:
        final_linked_list.append(i)
    return final_linked_list


if __name__ == "__main__":
    # Test case 1
    print('test 1')
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2
    print('test 2')

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))

    # Test case 3
    print('test 3')
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [1, 2, 3, 4]
    element_2 = [1, 2, 3]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))

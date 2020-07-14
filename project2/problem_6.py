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
    if llist_1.head == None:
        return llist_2
    if llist_2.head == None:
        return llist_1

    new_items = set()

    current = llist_1.head
    new_items.add(current.value)
    while current.next is not None:
        new_items.add(current.next.value)
        current = current.next

    current = llist_2.head
    new_items.add(current.value)
    while current.next is not None:
        new_items.add(current.next.value)
        current = current.next

    final_linked_list = LinkedList()
    for i in new_items:
        final_linked_list.append(i)
    return final_linked_list


def intersection(llist_1, llist_2):
    if llist_1.head == None:
        return LinkedList()
    if llist_2.head == None:
        return LinkedList()

    new_items1 = set()
    new_items2 = set()
    current = llist_1.head
    new_items1.add(current.value)
    while current.next is not None:
        new_items1.add(current.next.value)
        current = current.next
    current = llist_2.head
    new_items2.add(current.value)
    while current.next is not None:
        new_items2.add(current.next.value)
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

    print("union:", union(linked_list_1, linked_list_2))
    print("intersection:", intersection(linked_list_1, linked_list_2))
    # union: 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
    # intersection 4 -> 21 -> 6 ->

    # Test case 2
    print('test 2 have none in common, include some duplicated values')

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("union:", union(linked_list_3, linked_list_4))
    print("intersection:", intersection(linked_list_3, linked_list_4))
    # union: 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
    # # intersection []

    # Test case 3
    print('test 3 obvious common 1 2 3 and 4 to appear in union')
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [1, 2, 3, 4]
    element_2 = [1, 2, 3]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("union:", union(linked_list_3, linked_list_4))
    print("intersection:", intersection(linked_list_3, linked_list_4))
    # union: 1 -> 2 -> 3 -> 4 ->
    # intersection 1 -> 2 -> 3 ->

    # Test case 4
    print('test 4 one array empty')
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [1, 2, 3, 4]
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("union:", union(linked_list_3, linked_list_4))
    print("intersection:", intersection(linked_list_3, linked_list_4))
    # union: 1 -> 2 -> 3 -> 4 ->
    # intersection:

    # Test case 5
    print('test 5 the other array empty')
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = [1, 2, 3]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)
    print("union:", union(linked_list_3, linked_list_4))
    print("intersection:", intersection(linked_list_3, linked_list_4))
    # union: 1 -> 2 -> 3 ->
    # intersection:

    # Test case 6
    print('test 6 both empty')
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("union:", union(linked_list_3, linked_list_4))
    print("intersection:", intersection(linked_list_3, linked_list_4))
    # union:
    # intersection:

    # Test case 7
    print('test 7 all common')
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [1, 2, 3]
    element_2 = [1, 2, 3]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("union:", union(linked_list_3, linked_list_4))
    print("intersection:", intersection(linked_list_3, linked_list_4))
    # union: 1 -> 2 -> 3 ->
    # intersection: 1 -> 2 -> 3 ->

    # Test case 8
    print('test 8 big arrays')
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 4, 6, 34, 32, 6, 7, 78, 34,
                 33, 42, 56, 76, 83, 94, 88, 76543, 23456, 78, 79, 38, 765, 432, 3, 45]
    element_2 = [1, 2, 3, 6, 7, 78, 34, 32, 5, 5123,
                 32452456, 345345, 7857, 5, 345, 534, 6756746, 653]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("union:", union(linked_list_3, linked_list_4))
    print("intersection:", intersection(linked_list_3, linked_list_4))
    # union: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 5123 -> 6756746 -> 12 -> 653 -> 534 -> 32 -> 33 -> 34 -> 23456 -> 38 -> 42 -> 45 -> 345345 -> 432 -> 7857 -> 56 -> 76 -> 78 -> 79 -> 83 -> 88 -> 345 -> 94 -> 32452456 -> 765 -> 76543 ->
    # intersection: 32 -> 1 -> 2 -> 3 -> 34 -> 5 -> 6 -> 7 -> 78 ->

    # Test case 8
    print('test 8 array with one number')
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [21]
    element_2 = [1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("union:", union(linked_list_3, linked_list_4))
    print("intersection:", intersection(linked_list_3, linked_list_4))
    # union: 1 -> 21 ->
    # intersection:

    # Test case 9
    print('test 9 array with missing number')
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [21, ]
    element_2 = [1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("union:", union(linked_list_3, linked_list_4))
    print("intersection:", intersection(linked_list_3, linked_list_4))
    # union: 1 -> 21 ->
    # intersection:

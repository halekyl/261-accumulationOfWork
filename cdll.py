# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: #2 Part 3
# Description: Implementations of Deque and Bag ADT interfaces with a circular doubly linked list data
# structures. The implementation includes the following methods:add_front(), add_back(), insert_at_index(),
# remove_front(), remove_back(), remove_at_index(), get_front(), get_back(), remove(), count(), slice(), is_sorted()
# length(), is_empty(), swap_pairs(), reverse(), and sort().


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list (right after the front sentinel).
        """
        new_node = DLNode(value)
        new_node.prev = self.sentinel
        new_node.next =self.sentinel.next

        self.sentinel.next = new_node
        new_node.next.prev = new_node
        return

    def add_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list (right before the back sentinel).
        """
        new_node = DLNode(value)
        new_node.prev = self.sentinel.prev
        new_node.next = self.sentinel
        # loop to get last node
        self.sentinel.prev = new_node
        new_node.prev.next = new_node
        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the Circular list.
        If the provided index is invalid, the method raises a custom "CDLLException”.
        """
        if index < 0:
            raise CDLLException
        position = 0
        cur_node = self.sentinel
        # search for index to add new value after
        while position < index:
            cur_node = cur_node.next
            position += 1
            if cur_node == self.sentinel:
                raise CDLLException

        new_node = DLNode(value)
        new_node.next = cur_node.next
        new_node.prev = cur_node

        cur_node.next = new_node
        new_node.next.prev = new_node
        return

    def remove_front(self) -> None:
        """
        Removes the first node from the list.
        If the list is empty, the method raises a custom “CDLLException”.
        """
        if self.is_empty():
            raise CDLLException
        self.sentinel.next.next.prev = self.sentinel
        self.sentinel.next = self.sentinel.next.next
        return

    def remove_back(self) -> None:
        """
        Removes the last node from the list.
        If the list is empty, the method raises a custom “CDLLException”.
        """
        # empty list case
        if self.is_empty():
            raise CDLLException
        #remove back node, reset previous
        self.sentinel.prev.prev.next = self.sentinel
        self.sentinel.prev = self.sentinel.prev.prev
        return

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node from the list given its index.
        """
        if index < 0:
            raise CDLLException

        position = 0
        cur_node = self.sentinel
        # loop to find given index
        while position != index:
            cur_node = cur_node.next
            position += 1
            if cur_node.next == self.sentinel:
                raise CDLLException
        cur_node.next.next.prev = cur_node
        cur_node.next = cur_node.next.next
        return

    def get_front(self) -> object:
        """
        Returns value from the first node in the list without removing it.
        If the list is empty, the method raises a custom “CDLLException”.
        """
        if self.is_empty():
            raise CDLLException
        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        Returns value from the last node in the list without removing it.
        If the list is empty, the method raises a custom “CDLLException”.
        """
        if self.is_empty():
            raise CDLLException

        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        Traverses the list from the beginning to the end and removes the
        first node in the list that matches the provided “value” object.
        Returns True if some node was actually removed from the list.
        Otherwise it returns False.
        """
        if self.is_empty():
            return False
        curr = self.sentinel
        while curr.next != self.sentinel:
            if curr.next.value == value:
                curr.next = curr.next.next
                curr.next.prev = curr
                return True
            else:
                curr = curr.next
        return False

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided “value” object.
        """
        if self.is_empty():
            return 0

        match_count = 0
        element = self.sentinel

        while element.next != self.sentinel:
            if element.next.value == value:
                match_count += 1
            element = element.next
        return match_count

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new CircularList object that contains the requested number
        of nodes from the original list starting with the node located at the
        requested start index. If the provided start index is invalid, or if
        there are not enough nodes between start index and end of the list to
        make the slice of requested size, this method raises a custom “CDLLException”.
        """
        # To handle invalid indices
        if start_index < 0:
            raise CDLLException
        if size < 0:
            raise CDLLException
        cur_node = self.sentinel
        # To handle invalid index
        if cur_node.next.next is self.sentinel and index != (start_index - 1):
            raise CDLLException
        for index in range(start_index):
            cur_node = cur_node.next
        hold_index = start_index
        cdll_sliced = CircularList()
        while cur_node.next is not self.sentinel and hold_index < (start_index + size):
            cur_node = cur_node.next
            cdll_sliced.add_back(cur_node.value)
            hold_index += 1
        # To handle invalid slice size
        if (start_index + size) != hold_index:
            raise CDLLException
        return cdll_sliced

    def is_sorted(self) -> int:
        """
        Returns an integer that describes whether the linked list is sorted.
        Returns 1 if the list is sorted in strictly ascending order. Returns 2 if
        the list is sorted in strictly descending order. Otherwise returns 0.
        Empty list and list consisting of a single node is considered sorted
        in strictly ascending order.
        """
        if self.length() == 1:
            return 1
        ascending = True
        descending = True
        element = self.sentinel.next.next
        last_value = self.sentinel.next

        while element != self.sentinel:
            if element.value <= last_value.value:
                ascending = False
            if element.value >= last_value.value:
                descending = False
            element = element.next
            last_value = last_value.next

        if ascending:
            return 1
        elif descending:
            return 2
        else:
            return 0

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Swaps pairs of two nodes located at different indices by changing node pointers.
        If any of the provided indices is invalid, this raises a custom “CDLLException”.
        """
        if self.is_empty():
            raise CDLLException
        if index1 < 0:
            raise CDLLException
        if index2 < 0:
            raise CDLLException
        # Assign indices to use for searching
        low_index = index1
        high_index = index2
        if index1 > index2:
            low_index = index2
            high_index = index1
        # Traverse list to find the node indices matching indices input.
        cur_node = self.sentinel
        for index in range(high_index):
            cur_node = cur_node.next
            if index == 0:
                if low_index == 0:
                    node_1 = cur_node
            if index == low_index - 1:
                node_1 = cur_node.next

            if index == (high_index - 1):
                node_2 = cur_node.next
            # To handle invalid indices
            if cur_node.next.next is self.sentinel and index != (high_index - 1):
                raise CDLLException
                break
        # Change node pointers
        node_1_next = node_1.next
        node_1_prev = node_1.prev
        node_1.next = node_2.next
        node_1.next.prev = node_1
        node_1.prev = node_2.prev
        node_1.prev.next = node_1
        node_2.next = node_1_next
        node_2.next.prev = node_2
        node_2.prev = node_1_prev
        node_2.prev.next = node_2
        return

    def reverse(self) -> None:
        """
        Reverses the order of the nodes in the list “in place” without
        creating copies of nodes or existing list.
        """
        if self.is_empty() == True:
            return
        if self.length() == 1:
            return
        cur_node = self.sentinel.prev
        end_node = self.sentinel
        while cur_node.prev != self.sentinel:
            prev = cur_node.prev
            end_node.next = cur_node
            cur_node.prev = end_node
            end_node = cur_node
            cur_node = prev
        end_node.next = cur_node
        cur_node.prev = end_node
        cur_node.next = self.sentinel
        self.sentinel.prev = cur_node
        return

    def sort(self) -> None:
        """
        Sorts the content of the list in non-descending order, “in place” without
        creating copies of existing nodes or an existing list.
        """
        if self.is_empty() == True:
            return
        if self.length() == 1:
            return

        length = self.length() - 1
        while length > 0:
            elem_1 = self.sentinel.next
            elem_2 = elem_1.next
            compares = 0
            while compares < length:
                if elem_2.value < elem_1.value:
                    elem_1.next = elem_2.next
                    elem_2.prev = elem_1.prev
                    elem_2.next = elem_1
                    elem_1.prev = elem_2
                    elem_1.next.prev = elem_1
                    elem_2.prev.next = elem_2
                    elem_2 = elem_1.next
                    compares += 1
                else:
                    elem_1 = elem_2
                    elem_2 = elem_1.next
                    compares += 1
            length -= 1
        return

    def length(self) -> int:
        """
        Returns the number of nodes in the list.
        """
        number_nodes = 0
        cur = self.sentinel
        while cur.next != self.sentinel:
            cur = cur.next
            number_nodes += 1
        return number_nodes


    def is_empty(self) -> bool:
        """
        Returns True if the list has no actual nodes between sentinels. Otherwise, it returns False.
        """
        return self.sentinel.next == self.sentinel



#if __name__ == '__main__':
#    print('\n# add_front example 1')
#    list = CircularList()
#    print(list)
#    list.add_front('A')
#    list.add_front('B')
#    list.add_front('C')
#    print(list)


 #   print('\n# add_back example 1')
 #   list = CircularList()
 #   print(list)
 #   list.add_back('C')
 #   list.add_back('B')
 #   list.add_back('A')
 #   print(list)


 #   print('\n# insert_at_index example 1')
 #   list = CircularList()
 #   test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
 #   for index, value in test_cases:
 #       print('Insert of', value, 'at', index, ': ', end='')
 #       try:
 #           list.insert_at_index(index, value)
 #           print(list)
 #       except Exception as e:
 #           print(type(e))


#    print('\n# remove_front example 1')
#    list = CircularList([1, 2])
#    print(list)
#    for i in range(3):
#        try:
#            list.remove_front()
#            print('Successful removal', list)
#        except Exception as e:
#            print(type(e))


#    print('\n# remove_back example 1')
#    list = CircularList()
#    try:
#        list.remove_back()
#    except Exception as e:
#        print(type(e))
#    list.add_front('Z')
#    list.remove_back()
#    print(list)
#    list.add_front('Y')
#    list.add_back('Z')
#    list.add_front('X')
#    print(list)
#    list.remove_back()
#    print(list)


#    print('\n# remove_at_index example 1')
#    list = CircularList([1, 2, 3, 4, 5, 6])
#    print(list)
#    for index in [0, 0, 0, 2, 2, -2]:
#        print('Removed at index:', index, ': ', end='')
#        try:
#            list.remove_at_index(index)
#            print(list)
#        except Exception as e:
#            print(type(e))
#    print(list)


#    print('\n# get_front example 1')
#    list = CircularList(['A', 'B'])
#    print(list.get_front())
#    print(list.get_front())
#    list.remove_front()
#    print(list.get_front())
#    list.remove_back()
#    try:
#        print(list.get_front())
#    except Exception as e:
#        print(type(e))


#    print('\n# get_back example 1')
#    list = CircularList([1, 2, 3])
#    list.add_back(4)
#    print(list.get_back())
#    list.remove_back()
#    print(list)
#    print(list.get_back())


#    print('\n# remove example 1')
#    list = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
#    print(list)
#    for value in [7, 3, 3, 3, 3]:
#        print(list.remove(value), list.length(), list)


#    print('\n# count example 1')
#    list = CircularList([1, 2, 3, 1, 2, 2])
#    print(list, list.count(1), list.count(2), list.count(3), list.count(4))


#    print('\n# slice example 1')
#    list = CircularList([1, 2, 3, 4, 5, 6, 7, 8, 9])
#    ll_slice = list.slice(1, 3)
#    print(list, ll_slice, sep="\n")
#    ll_slice.remove_at_index(0)
#    print(list, ll_slice, sep="\n")


#    print('\n# slice example 2')
#    list = CircularList([10, 11, 12, 13, 14, 15, 16])
#    print("SOURCE:", list)
#    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
#    for index, size in slices:
#        print("Slice", index, "/", size, end="")
#        try:
#            print(" --- OK: ", list.slice(index, size))
#        except:
#            print(" --- exception occurred.")


#    print('\n# is_sorted example 1')
#    test_cases = (
#        [-100, -8, 0, 2, 3, 10, 20, 100],
#        ['A', 'B', 'Z', 'a', 'z'],
#        ['Z', 'T', 'K', 'A', '1'],
#        [1, 3, -10, 20, -30, 0],
#        [-10, 0, 0, 10, 20, 30],
#        [100, 90, 0, -90, -200]
#    )
#    for case in test_cases:
#        list = CircularList(case)
#        print('Result:', list.is_sorted(), list)


#    print('\n# is_empty example 1')
#    list = CircularList()
#    print(list.is_empty(), list)
#    list.add_back(100)
#    print(list.is_empty(), list)
#    list.remove_at_index(0)
#    print(list.is_empty(), list)


#    print('\n# length example 1')
#    list = CircularList()
#    print(list.length())
#    for i in range(800):
#        list.add_front(i)
#    print(list.length())
#    for i in range(799, 300, -1):
#        list.remove_at_index(i)
#    print(list.length())

#    print('\n# swap_pairs example 1')
#    list = CircularList([0, 1, 2, 3, 4, 5, 6])
#    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5), (4, 2), (3, 3))

#    for i, j in test_cases:
#        print('Swap nodes ', i, j, ' ', end='')
#        try:
#            list.swap_pairs(i, j)
#            print(list)
#        except Exception as e:
#            print(type(e))


#    print('\n# reverse example 1')
#    test_cases = (
#        [1, 2, 3, 3, 4, 5],
#        [1, 2, 3, 4, 5],
#        ['A', 'B', 'C', 'D']
#    )
#    for case in test_cases:
#        list = CircularList(case)
#        list.reverse()
#        print(list)


#    print('\n# reverse example 2')
#    list = CircularList()
#    print(list)
#    list.reverse()
#    print(list)
#    list.add_back(2)
#    list.add_back(3)
#    list.add_front(1)
#    list.reverse()
#    print(list)


#    print('\n# sort example 1')
#    test_cases = (
#        [1, 10, 2, 20, 3, 30, 4, 40, 5],
#        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
#        [(1, 1), (20, 1), (1, 20), (2, 20)]
#    )
#    for case in test_cases:
#        list = CircularList(case)
#        print(list)
#        list.sort()
#        print(list)
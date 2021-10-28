# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: #3 Part 2 max_stack_sll
# Description: Implementation of a Stack ADT class while using the LinkedList data structure from part 1
# as underlying data storage for your Stack ADT.


from sll import *


class StackException(Exception):
    """
    Custom exception to be used by MaxStack Class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new MaxStack based on Singly Linked Lists
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sll_val = LinkedList()
        self.sll_max = LinkedList()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.sll_val.length()) + " elements. "
        out += str(self.sll_val)
        return out

    def push(self, value: object) -> None:
        """
        Adds a new element to the top of the stack. It must be implemented with O(1) runtime complexity.
        """

        self.sll_val.add_front(value)

        # to handle empty max list
        if self.sll_max.is_empty():
            self.sll_max.add_front(value)

        if self.sll_max.get_front() < value:
            self.sll_max.add_front(value)
        else:
            self.sll_max.add_front(self.sll_max.get_front())
        return

    def pop(self) -> object:
        """
        Removes the top element from the stack and returns its value.
        If the stack is empty, the method raises a custom “StackException”.
        """
        if self.sll_val.is_empty():
            raise StackException

        self.sll_max.remove_front()

        top_elem_value = self.sll_val.get_front()
        self.sll_val.remove_front()
        return top_elem_value

    def top(self) -> object:
        """
        Returns the value of the top element of the stack without removing it.
        If the stack is empty, the method raises a custom “StackException”.
        """
        if self.sll_val.is_empty():
            raise StackException
        top_elem_value = self.sll_val.get_front()
        return top_elem_value

    def is_empty(self) -> bool:
        """
        Returns True if there are no elements in the stack. Otherwise it returns False.
        """
        return self.sll_val.is_empty()

    def size(self) -> int:
        """
        Returns the number of elements currently in the stack.
        """
        num_of_elements = self.sll_val.length()
        return num_of_elements

    def get_max(self) -> object:
        """
        Returns the maximum value currently stored in the stack.
        If the stack is empty, the method raises a custom “StackException”.
        """
        if self.sll_val.is_empty():
            raise StackException
        max_value = self.sll_max.get_front()
        return max_value


# BASIC TESTING
#if __name__ == "__main__":
#    print('\n# push example 1')
#    s = MaxStack()
#    print(s)
#    for value in [1, 2, 3, 4, 5]:
#        s.push(value)
#    print(s)


#    print('\n# pop example 1')
#    s = MaxStack()
#    try:
#        print(s.pop())
#    except Exception as e:
#        print("Exception:", type(e))
#    for value in [1, 2, 3, 4, 5]:
#        s.push(value)
#    for i in range(6):
#        try:
#            print(s.pop())
#        except Exception as e:
#            print("Exception:", type(e))


#    print('\n# top example 1')
#    s = MaxStack()
#    try:
#        s.top()
#    except Exception as e:
#        print("No elements in stack", type(e))
#    s.push(10)
#    s.push(20)
#    print(s)
#    print(s.top())
#    print(s.top())
#    print(s)


#    print('\n# is_empty example 1')
#    s = MaxStack()
#    print(s.is_empty())
#    s.push(10)
#    print(s.is_empty())
#    s.pop()
#    print(s.is_empty())


#    print('\n# size example 1')
#    s = MaxStack()
#    print(s.size())
#    for value in [1, 2, 3, 4, 5]:
#        s.push(value)
#    print(s.size())


#    print('\n# get_max example 1')
#    s = MaxStack()
#    for value in [1, -20, 15, 21, 21, 40, 50]:
#        print(s, ' ', end='')
#        try:
#            print(s.get_max())
#        except Exception as e:
#            print(type(e))
#        s.push(value)
#    while not s.is_empty():
#        print(s.size(), end='')
#        print(' Pop value:', s.pop(), ' get_max after: ', end='')
#        try:
#            print(s.get_max())
#        except Exception as e:
#            print(type(e))
# Course: CS261 - Data Structures
# Assignment: 5
# Student: Kylee Hale
# Description: Implementation of MinHeap class.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap maintaining heap property.
        """
        #Mark current index
        c_index = self.heap.length()
        #Put new element at the end of the array.
        self.heap.append(node)
        #Compute parent index
        p_index = (c_index - 1) // 2
        #Compare value of inserted element with value of its parent.
        #If parent value greater than value of inserted element = swap.
        #or if reach beggining of array = stop.
        while self.heap.get_at_index(p_index) > node and (p_index >= 0):
            self.heap.swap(p_index, c_index)
            c_index = p_index
            p_index = (c_index - 1) // 2
        return

    def get_min(self) -> object:
        """
        Returns an object with a minimum key without removing it from the heap.
        """
        #If heap is empty, raises Exception.
        if self.is_empty():
            raise MinHeapException
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Returns an object with a minimum key and removes it from the heap.
        """
        # If heap is empty, raises Exception.
        if self.is_empty():
            raise MinHeapException

        #Var = to remember the value of first element in array (to be returned later)
        first_node = self.heap.get_at_index(0)
        #Remove the last element
        replacement_node = self.heap.pop()
        #Replace the value of the first element in the array with the value of the last element
        if not self.is_empty():
            self.heap.set_at_index(0, replacement_node)
        #Array is not empty so compute indices of children of the replacement element
            index = 0                   # i
            lc_index = 1                        # 2*i+1
            rc_index = 2                        # 2*i+2
            last_index = self.heap.length() - 1
            # while processing = true loop continues as swaps continue and move node to correct index
            processing = True
            while processing:
                # If both child indices fall beyond the array bounds of array = stop here
                if lc_index > last_index and rc_index > last_index:
                    processing = False
                #if left is beyond bounds compare just right child:
                elif lc_index > last_index:
                    #If the replacement element’s value is less than right child
                    # swap these two elements.
                    if replacement_node > self.heap.get_at_index(rc_index):
                        self.heap.swap(index, rc_index)
                        index = rc_index
                    else:
                        processing = False
                #if right is beyond bounds compare just left child:
                elif rc_index > last_index:
                    #If the replacement element’s value is less than right child
                    # swap these two elements.
                    if replacement_node > self.heap.get_at_index(lc_index):
                        self.heap.swap(index, lc_index)
                        index = lc_index
                    else:
                        processing = False
                # compare both left & right
                else:
                    lc_node = self.heap.get_at_index(lc_index)
                    rc_node = self.heap.get_at_index(rc_index)
                    #determine smaller of the two children to compare
                    if lc_node < rc_node:
                        if replacement_node > lc_node:
                            self.heap.swap(index, lc_index)
                            index = lc_index
                        else:
                            processing = False
                    else:
                        if replacement_node > rc_node:
                            self.heap.swap(index, rc_index)
                            index = rc_index
                        else:
                            processing = False
                #indices for next round through loop
                lc_index = (index * 2) + 1
                rc_index = (index * 2) + 2
        return first_node

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a dynamic array with objects in any order and builds a proper MinHeap from them.
        """
        self.heap = DynamicArray()
        length = da.length()

        if length == 0:  #if Empty, do nothing
            return
        #append elements from array to heap
        array_index = 0
        while array_index < length:
            self.heap.append(da.get_at_index(array_index))
            array_index += 1
        #look for first non leaf element
        starting_index = (length - 2) // 2  #index to begin sort
        while starting_index >= 0:
            replacement_node = self.heap.get_at_index(starting_index)
            # just like when removing min.
            # Array is not empty so compute indices of children of the replacement element
            index = starting_index  # i
            lc_index = (index * 2) + 1  # 2*i+1
            rc_index = (index * 2) + 2  # 2*i+2
            last_index = length - 1
            # while processing = true loop continues as swaps continue and move node to correct index
            processing = True
            while processing:
                # If both child indices fall beyond the array bounds of array = stop here
                if lc_index > last_index and rc_index > last_index:
                    processing = False
                # if left is beyond bounds compare just right child:
                elif lc_index > last_index:
                    # If the replacement element’s value is less than right child
                    # swap these two elements.
                    if replacement_node > self.heap.get_at_index(rc_index):
                        self.heap.swap(index, rc_index)
                        index = rc_index
                    else:
                        processing = False
                # if right is beyond bounds compare just left child:
                elif rc_index > last_index:
                    # If the replacement element’s value is less than right child
                    # swap these two elements.
                    if replacement_node > self.heap.get_at_index(lc_index):
                        self.heap.swap(index, lc_index)
                        index = lc_index
                    else:
                        processing = False
                # compare both left & right
                else:
                    lc_node = self.heap.get_at_index(lc_index)
                    rc_node = self.heap.get_at_index(rc_index)
                    # determine smaller of the two children to compare
                    if lc_node < rc_node:
                        if replacement_node > lc_node:
                            self.heap.swap(index, lc_index)
                            index = lc_index
                        else:
                            processing = False
                    else:
                        if replacement_node > rc_node:
                            self.heap.swap(index, rc_index)
                            index = rc_index
                        else:
                            processing = False
                # indices for next round through loop
                lc_index = (index * 2) + 1
                rc_index = (index * 2) + 2
            starting_index -= 1
        return

# BASIC TESTING
#if __name__ == '__main__':

#    print("\nPDF - add example 1")
#    print("-------------------")
#    h = MinHeap()
#    print(h, h.is_empty())
#    for value in range(300, 200, -15):
#        h.add(value)
#        print(h)

#    print("\nPDF - add example 2")
#    print("-------------------")
#    h = MinHeap(['fish', 'bird'])
#    print(h)
#    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
#        h.add(value)
#        print(h)


#    print("\nPDF - get_min example 1")
#    print("-----------------------")
#    h = MinHeap(['fish', 'bird'])
#    print(h)
#    print(h.get_min(), h.get_min())


#    print("\nPDF - remove_min example 1")
#    print("--------------------------")
#    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
#    while not h.is_empty():
#        print(h, end=' ')
#        print(h.remove_min())


#    print("\nPDF - build_heap example 1")
#    print("--------------------------")
#    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
#    h = MinHeap(['zebra', 'apple'])
#    print(h)
#    h.build_heap(da)
#    print(h)
#    da.set_at_index(0, 500)
#    print(da)
#    print(h)

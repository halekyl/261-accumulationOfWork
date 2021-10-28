# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: #4 bst
# Description: Implement a BST class with methods add(), contains(), remove()
# # get_first(), remove_first(), pre_order_traversal(), in_order_traversal()
# # post_order_traversal(), by_level_traversal(), size(), height()
# # count_leaves(), count_unique(), is_complete(), is_full(), is_perfect()


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        if cur.left:
            self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        if cur.right:
            self._str_helper(cur.right, values)

    def add(self, value: object) -> None:
        """
        Adds new value to the tree, maintaining BST property.
        Duplicates are allowed and placed in the right subtree.
        """
        incoming_node = TreeNode(value) #new value being added
        parent = None
        current_node = self.root
        # search tree for where to add new value
        while current_node is not None:
            parent = current_node
            if incoming_node.value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        # to handle empty tree case
        if parent is None:
            self.root = incoming_node
        # add new value
        elif incoming_node.value < parent.value:
            parent.left = incoming_node
        else:
            parent.right = incoming_node
        pass

    def contains(self, value: object) -> bool:
        """
        Returns True if the value parameter is in the BinaryTree or
        False if it is not in the tree. If the tree is empty, returns False.
        """
        current_node = self.root
        # if empty tree jump to return False
        while current_node is not None:
            # search for value in tree
            if current_node.value == value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        # value not in tree
        return False

    def get_first(self) -> object:
        """
        Returns the value stored at the root node.
        If the BinaryTree is empty, returns None.
        """
        # handles empty tree case
        if self.root is None:
            return None
        else:
            return self.root.value

    def remove_first(self) -> bool:
        """
        Removes the root node in the BinaryTree. Returns False if the tree is empty
        and there is no root node to remove and True if the root is removed.
        """
        # handles empty tree case
        if self.root is None:
            return False
        else:
            # no children update root to none
            if self.root.left is None and self.root.right is None:
                    self.root = None
                    return True
            # root has one child
            elif self.root.right is None:
                self.root = self.root.left
                return True
            else:
                # has both children

                # find in-order successor
                in_ord_succ = self.get_left(self.root.right)
                # find in-order successor parent call get_parent()
                parent = self.get_parent(in_ord_succ)

                if parent == self.root:
                    in_ord_succ.left = self.root.left
                    # root removed return
                    self.root = in_ord_succ
                    return True
                else:
                    in_ord_succ.left = self.root.left
                    parent.left = in_ord_succ.right
                    in_ord_succ.right = self.root.right
                    # root removed return
                    self.root = in_ord_succ
                    return True

    def remove(self, value) -> bool:
        """
        Remove the first instance of the object in the BinaryTree.
        Returns True if the value is removed from the BinaryTree and otherwise returns False.
        NOTE: See ‘Specific Instructions’ for explanation of which node replaces the deleted node.
        """
        # value is the root case
        if value == self.root.value:
            self.remove_first()
            return True

        # search tree for node matching value
        if self.contains(value):
            current_node = self.root
            while current_node.value != value:
                if value < current_node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
        else:
            return False

        # parent of value node match
        curr_node_parent = self.get_parent(current_node)
        # in case of no children, current node parent is None
        if current_node.left is None and current_node.right is None:
            if current_node.value < curr_node_parent.value:
                curr_node_parent.left = None
            else:
                curr_node_parent.right = None
        else:
            # find in-order successor
            # in case of no right node left moves up then return
            if current_node.right is None:
                # in-order successor
                in_ord_succ = current_node.left
                if current_node.value < curr_node_parent.value:
                    curr_node_parent.left = in_ord_succ
                else:
                    curr_node_parent.right = in_ord_succ
                # free the node
                current_node.left = None
                current_node.right = None
                return True
            else:
                in_ord_succ = self.get_left(current_node.right)

            # find in-order successor parent call get_parent()
            in_ord_succ_parent = self.get_parent(in_ord_succ)
            in_ord_succ.left = current_node.left
            if in_ord_succ is not current_node.right:
                in_ord_succ_parent.left = in_ord_succ.right
                in_ord_succ.right = current_node.right

            # update parent node to in-order successor
            if current_node.value < curr_node_parent.value:
                curr_node_parent.left = in_ord_succ
            else:
                curr_node_parent.right = in_ord_succ
        # free the node
        current_node.left = None
        current_node.right = None
        return True

    def pre_order_traversal(self) -> Queue:
        """
        Performs pre-order traversal of the tree and returns a
        Queue object that contains values of visited nodes, in the order they were visited.
        """
        visited = Queue()
        self.pre_order_traversal_helper(self.root, visited)
        return visited

    def pre_order_traversal_helper(self, current_node=None, visited=None) -> Queue:
        """
        Helper method for pre_order_traversal()
        """
        # base case empty tree
        if current_node is None:
            return visited
        # NLR – process current node before going onto subtrees
        visited.enqueue(current_node.value)
        # left then right and return
        self.pre_order_traversal_helper(current_node.left, visited)
        self.pre_order_traversal_helper(current_node.right, visited)
        return visited

    def in_order_traversal(self) -> Queue:
        """
        Performs in-order traversal of the tree and returns a Queue object that contains
        values of visited nodes, in the order they were visited.
        """
        visited = Queue()
        self.in_order_traversal_helper(self.root, visited)
        return visited

    def in_order_traversal_helper(self, current_node=None, visited=None) -> Queue:
        """
        Helper method for in_order_traversal()
        """
        # base case empty tree
        if current_node is None:
            return visited
        # LNR go to current node’s left subtree before processing current node
        self.in_order_traversal_helper(current_node.left, visited)
        visited.enqueue(current_node.value)
        # then go to node’s right subtree and return
        self.in_order_traversal_helper(current_node.right, visited)
        return visited

    def post_order_traversal(self) -> Queue:
        """
        Performs post-order traversal of the tree and returns a Queue object that contains
        values of visited nodes, in the order they were visited.
        """
        visited = Queue()
        self.post_order_traversal_helper(self.root, visited)
        return visited

    def post_order_traversal_helper(self, current_node=None, visited=None) -> Queue:
        """
        Helper method for post_order_traversal.
        """
        # base case empty tree
        if current_node is None:
            return visited
        # LRN visit both left & right subtrees
        self.post_order_traversal_helper(current_node.left, visited)
        self.post_order_traversal_helper(current_node.right, visited)
        # then process node and return
        visited.enqueue(current_node.value)
        return visited

    def by_level_traversal(self) -> Queue:
        """
        Performs by-level traversal of the tree and returns a Queue object that contains
        values of visited nodes, in the order they were visited.
        """
        tree_queue = Queue()
        visited = Queue()
        # empty tree case
        if self.root is None:
            return visited
        # begin with root node
        tree_queue.enqueue(self.root)
        while not tree_queue.is_empty():
            current_node = tree_queue.dequeue()
            # process left to right level by level
            if current_node is not None:
                visited.enqueue(current_node)
                tree_queue.enqueue(current_node.left)
                tree_queue.enqueue(current_node.right)
        return visited

    def is_full(self) -> bool:
        """
        Returns True if the current tree is a ‘full binary tree’. Empty tree is considered ‘full’.
        Tree consisting of a single root node is ‘full’.
        """
        # empty tree case
        if self.root is None:
            return True
        # just a root in tree case
        if self.root.left is None and self.root.right is None:
            return True
        return self.is_full_helper(self.root)

    def is_full_helper(self, node: object) -> bool:
        """
        Helper method for is_full().
        """
        # leaf case no children
        if node.left is None and node.right is None:
            return True
        # children on left and right and full trees
        if node.left is not None and node.right is not None:
            return (self.is_full_helper(node.left) and self.is_full_helper(node.right))
        return False

    def is_complete(self) -> bool:
        """
        Returns True if the current tree is a ‘complete binary tree’. Empty tree is
        considered complete. Tree consisting of a single root node is complete.
        """
        # empty tree is considered complete
        if self.root is None:
            return True

        queue = Queue()
        queue.enqueue(self.root)
        # set to True when a sign of an incomplete tree is found
        sign_of_complete = False
        # being traversal starting with root
        while not queue.is_empty():
            current_node = queue.dequeue()
            if not sign_of_complete:
                # case of no left child, only right child present
                if current_node.left is None and current_node.right is not None:
                    return False
                # tree of just a root is considered complete
                elif current_node.left is None and current_node.right is None:
                    sign_of_complete = True
                # case of only left child, no right child present is complete
                elif current_node.left is not None and current_node.right is None:
                    sign_of_complete = True
                    queue.enqueue(current_node.left)
                # case of both left and right children present
                if not sign_of_complete and current_node.left is not None and current_node.right is not None:
                    queue.enqueue(current_node.left)
                    queue.enqueue(current_node.right)
            elif sign_of_complete:
                if current_node.left is None and current_node.right is not None:
                    return False
                if current_node.left is not None and current_node.right is None:
                    return False
        # is it complete
        return True

    def is_perfect(self) -> bool:
        """
        Returns True if the current tree is a ‘perfect binary tree’. Empty tree is
        considered ‘perfect’. Tree consisting of a single root node is ‘perfect’.
        """
        # single root case is perfect
        if self.root is None:
            return True
        depth = self.get_depth(self.root)
        return self.is_perfect_helper(self.root, depth)

    def is_perfect_helper(self, node: object, depth: int, level=0):
        """
        Helper method for is_perfect()
        """
        # leaf node must be same depth as others
        if (node.left == None and node.right == None):
            return (depth == level + 1)
        # inside node and one of the children is empty
        if (node.left == None and node.right != None):
            return False
        if (node.left != None and node.right == None):
            return False
        # check if both left and right are perfect
        return (self.is_perfect_helper(node.left, depth, level + 1) and self.is_perfect_helper(node.right, depth,
                                                                                               level + 1))
    def size(self) -> int:
        """
        Returns the total number of nodes in the tree.
        """
        size = 0
        # to handle empty tree
        if self.root is None:
            return size
        return self.size_helper(self.root)

    def size_helper(self, node: object) -> int:
        """
        Helper method for size()
        """
        # if not empty start size = 1 for root
        size = 1
        # start with root count size of left side
        if node.left is not None:
            size += self.size_helper(node.left)
        # count size of right side
        if node.right is not None:
            size += self.size_helper(node.right)
        return size

    def height(self) -> int:
        """
        Returns the height of the binary tree. Empty tree has a height of -1. Tree consisting
        of just a single root node should return a height of 0.
        """
        # empty tree case
        if self.root is None:
            return -1
        return self.height_helper(self.root)

    def height_helper(self, node: object) -> int:
        # leaf case
        if node.left is None and node.right is None:
            return 0

        # cases with just one child
        # determine which left or right height to return
        if node.left is None and node.right is not None:
            return self.height_helper(node.right) + 1
        if node.left is not None and node.right is None:
            return self.height_helper(node.left) + 1

        # both children present determine larger and return
        if self.height_helper(node.left) > self.height_helper(node.right):
            return self.height_helper(node.left) + 1
        else:
            return self.height_helper(node.right) + 1

    def count_leaves(self) -> int:
        """
        Returns the number of nodes in the tree that have no children. If the tree is empty,
        this method should return 0.
        """
        # empty case
        if self.root is None:
            return 0

        return self.count_leaves_helper(self.root)

    def count_leaves_helper(self, node: object) -> int:
        """
        Helper method for count_leaves()
        """
        # first leaf case
        if node.left is None and node.right is None:
            return 1
        # just a right child
        if node.left is None and node.right is not None:
            return self.count_leaves_helper(node.right)
        # just a left child
        if node.left is not None and node.right is None:
            return self.count_leaves_helper(node.left)
        # both left and right children
        left = self.count_leaves_helper(node.left)
        right = self.count_leaves_helper(node.right)
        return left + right

    def count_unique(self) -> int:
        """
        Returns the count of unique values stored in the tree. If all values stored in the tree
        are distinct (no duplicates), this method will return the same result as the size() method.
        """
        # empty tree
        if self.root is None:
            return 0
        queue = Queue()
        return self.count_unique_helper(self.root, queue)

    def count_unique_helper(self, node: object, queue: object) -> int:
        """
        Helper method for count_unique.
        """
        # use queue to iterate through values starting with root
        queue.enqueue(node)
        unique_count = 0
        while not queue.is_empty():
        #use dequeue to take away value from queue to compare if any other values match
            node = queue.dequeue()
        # check for instance of the value
        # unique count records last instance of value.
            if node:
                if not node.right:
                    unique_count += 1
                elif (node.right.value != node.value) and not node.right.left:
                    unique_count += 1
                elif (node.right.value != node.value) and node.right.left:
                    temp_node = node.right.left

                    while temp_node.left:
                        temp_node = temp_node.left

                    if node.value != temp_node.value:
                        unique_count += 1
                queue.enqueue(node.left)
                queue.enqueue(node.right)
        return unique_count


    def get_parent(self, node: object):
        """
        Returns the parent of node given. If no children returns False.
        Used with remove_first() and remove().
        """
        # empty tree case
        if node is self.root:
            return None
        else:
            current_node = self.root
            while current_node is not node:
                if node.value < current_node.value:
                    if current_node.left.value == node.value:
                        return current_node
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right.value == node.value:
                        return current_node
                    else:
                        current_node = current_node.right
            return False

    def get_left(self, node: object) -> object:
        """
        Returns the leftmost child in tree.
        """
        #traverse through left side
        while node.left is not None:
            node = node.left
        return node

    def get_depth(self, node: object) -> int:
        """
        Returns the depth of the leftmost leaf.
        """
        depth = 0
        while (node != None):
            depth += 1
            node = node.left
        return depth



# BASIC TESTING - PDF EXAMPLES

#if __name__ == '__main__':
#    """ add() example #1 """
#    print("\nPDF - method add() example 1")
#    print("----------------------------")
#    tree = BST()
#    print(tree)
#    tree.add(10)
#    tree.add(15)
#    tree.add(5)
#    print(tree)
#    tree.add(15)
#    tree.add(15)
#    print(tree)
#    tree.add(5)
#    print(tree)

#    """ add() example 2 """
#    print("\nPDF - method add() example 2")
#    print("----------------------------")
#    tree = BST()
#    tree.add(10)
#    tree.add(10)
#    print(tree)
#    tree.add(-1)
#    print(tree)
#    tree.add(5)
#    print(tree)
#    tree.add(-1)
#    print(tree)

#    """ contains() example 1 """
#    print("\nPDF - method contains() example 1")
#    print("---------------------------------")
#    tree = BST([10, 5, 15])
#    print(tree.contains(15))
#    print(tree.contains(-10))
#    print(tree.contains(15))

#    """ contains() example 2 """
#    print("\nPDF - method contains() example 2")
#    print("---------------------------------")
#    tree = BST()
#    print(tree.contains(0))

#    """ get_first() example 1 """
#    print("\nPDF - method get_first() example 1")
#    print("----------------------------------")
#    tree = BST()
#    print(tree.get_first())
#    tree.add(10)
#    tree.add(15)
#    tree.add(5)
#    print(tree.get_first())
#    print(tree)

#    """ remove() example 1 """
#    print("\nPDF - method remove() example 1")
#    print("-------------------------------")
#    tree = BST([10, 5, 15])
#    print(tree.remove(7))
#    print(tree.remove(15))
#    print(tree.remove(15))

#    """ remove() example 2 """
#    print("\nPDF - method remove() example 2")
#    print("-------------------------------")
#    tree = BST([10, 20, 5, 15, 17, 7, 12])
#    print(tree.remove(20))
#    print(tree)

#    """ remove() example 3 """
#    print("\nPDF - method remove() example 3")
#    print("-------------------------------")
#    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
#    print(tree.remove(20))
#    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
#    print(tree.pre_order_traversal())
#    print(tree.in_order_traversal())
#    print(tree.post_order_traversal())
#    print(tree.by_level_traversal())

#    """ remove_first() example 1 """
#    print("\nPDF - method remove_first() example 1")
#    print("-------------------------------------")
#    tree = BST([10, 15, 5])
#    print(tree.remove_first())
#    print(tree)

#    """ remove_first() example 2 """
#    print("\nPDF - method remove_first() example 2")
#    print("-------------------------------------")
#    tree = BST([10, 20, 5, 15, 17, 7])
#    print(tree.remove_first())
#    print(tree)

#    """ remove_first() example 3 """
#    print("\nPDF - method remove_first() example 3")
#    print("-------------------------------------")
#    tree = BST([10, 10, -1, 5, -1])
#    tree = BST([10, 10, -1, 5, -1])
#    print(tree.remove_first(), tree)
#    print(tree.remove_first(), tree)
#    print(tree.remove_first(), tree)
#    print(tree.remove_first(), tree)
#    print(tree.remove_first(), tree)
#    print(tree.remove_first(), tree)

#    """ Traversal methods example 1 """
#    print("\nPDF - traversal methods example 1")
#    print("---------------------------------")
#    tree = BST([10, 20, 5, 15, 17, 7, 12])
#    print(tree.pre_order_traversal())
#    print(tree.in_order_traversal())
#    print(tree.post_order_traversal())
#    print(tree.by_level_traversal())

#    """ Traversal methods example 2 """
#    print("\nPDF - traversal methods example 2")
#    print("---------------------------------")
#    tree = BST([10, 10, -1, 5, -1])
#    print(tree.pre_order_traversal())
#    print(tree.in_order_traversal())
#    print(tree.post_order_traversal())
#    print(tree.by_level_traversal())

#    """ Comprehensive example 1 """
#    print("\nComprehensive example 1")
#    print("-----------------------")
#    tree = BST()
#    header = 'Value   Size  Height   Leaves   Unique   '
#    header += 'Complete?  Full?    Perfect?'
#    print(header)
#    print('-' * len(header))
#    print(f'  N/A {tree.size():6} {tree.height():7} ',
#          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
#          f'{str(tree.is_complete()):10}',
#          f'{str(tree.is_full()):7} ',
#          f'{str(tree.is_perfect())}')

#    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
#        tree.add(value)
#        print(f'{value:5} {tree.size():6} {tree.height():7} ',
#              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
#              f'{str(tree.is_complete()):10}',
#              f'{str(tree.is_full()):7} ',
#              f'{str(tree.is_perfect())}')
#   print()
#    print(tree.pre_order_traversal())
#    print(tree.in_order_traversal())
#    print(tree.post_order_traversal())
#    print(tree.by_level_traversal())

#    """ Comprehensive example 2 """
#    print("\nComprehensive example 2")
#    print("-----------------------")
#    tree = BST()
#    header = 'Value   Size  Height   Leaves   Unique   '
#    header += 'Complete?  Full?    Perfect?'
#    print(header)
#    print('-' * len(header))
#    print(f'N/A   {tree.size():6} {tree.height():7} ',
#          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
#          f'{str(tree.is_complete()):10}',
#          f'{str(tree.is_full()):7} ',
#          f'{str(tree.is_perfect())}')

#    for value in 'DATA STRUCTURES':
#        tree.add(value)
#        print(f'{value:5} {tree.size():6} {tree.height():7} ',
#              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
#              f'{str(tree.is_complete()):10}',
#              f'{str(tree.is_full()):7} ',
#              f'{str(tree.is_perfect())}')
#    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
#          tree.post_order_traversal(), tree.by_level_traversal(),
#          sep='\n')


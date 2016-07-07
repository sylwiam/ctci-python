# Python program to find predecessor and successor in a BST
from binary_tree import BinaryTree

# A BST node
class Node:

    # Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.value)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret

def findPreSuc(node, value):
    """ This function finds predecessor and successor of value in BST
    It sets pre and suc as predecessor and successor respectively
    """

    # Base Case
    if node is None:
        return

    # If value is present at node
    if node.value == value:
        # the maximum value in left subtree is predecessor
        # if node.left is not None:
        #     print "IF node.left is not None"
        #     tmp = node.left
        #     while(tmp.right):
        #         tmp = tmp.right
        #     findPreSuc.pre = tmp

        # the minimum value in right subtree is successor
        if node.right is not None:
            tmp = node.right
            while(tmp.left):
                tmp = tmp.left
            findPreSuc.suc = tmp

        return

    if node.value > value:  # If value is smaller than node's value, go to left subtree
        findPreSuc.suc = node
        findPreSuc(node.left, value)

    # else:  # go to right subtree
    #     print "ELSE (node.value < value) "
    #     findPreSuc.pre = node
    #     findPreSuc(node.right, value)

def insert(node, value):
    """ A utility function to insert a new node in with given value in BST
    """
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)

    else:
        node.right = insert(node.right, value)

    return node


# Driver program to test above function
value = 30  #Key to be searched in BST

""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 
"""
root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

print root
findPreSuc.suc = None

findPreSuc(root, value)

print "----"

if findPreSuc.suc is not None:
    print "Successor is", findPreSuc.suc.value
else:
    print "No Successor"

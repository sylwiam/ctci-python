"""
Implement a function to check if a binary tree is balanced. For the purposes
of this question, a balanced tree is defined to be a tree such that the heights
of the two subtrees of any node never differ by more than one.
"""

from binary_tree import BinaryTree
import random

root = BinaryTree(random.randint(0,20))
stack = [root]
for i in range(0, 3):
    current_node = stack.pop()
    current_node.left = BinaryTree(random.randint(0,20))
    current_node.right = BinaryTree(random.randint(0,20))
    stack.insert(0, current_node.left)
    stack.insert(0, current_node.right)

print root


def is_BST(node):
    if node is not None:      
        is_BST(node.left)
        print node.value
        is_BST(node.right)
                       

if __name__ == '__main__':
    print is_BST(root)

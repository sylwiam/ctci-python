import random

""" Given a binary tree, design an algorithm which creates a linked list of all the
nodes at each depth (e.g. if you have a tree with depth D , you'll have D linked lists).
"""
#binary tree python
class BinaryTree:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None

    def __str__(self):
        return "( " + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

class LinkedList:
    def __init__(self,content):
        self.content = content
        self.next = None

    def __str__(self):
        return "( " + str(self.content) + str(self.next) + " )"
    
def generate_tree_depth_lists():
    

def generate_linked_lists():

#building testcase 1
def make_random_balanced_tree(depth):
    if depth>0:
        tree = BinaryTree(random.randint(0, 100))
        tree.left = make_random_balanced_tree(depth-1)
        tree.right = make_random_balanced_tree(depth-1)
        return tree
    else:
        return None

balanced_tree = make_random_balanced_tree(5)


#testing

print balanced_tree

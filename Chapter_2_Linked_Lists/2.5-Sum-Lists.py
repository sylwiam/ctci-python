""" 
2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit
  The digits are stored in reverse order, such that the 1's digit is at the head of the list
  Write a function that adds the two numbers and returns the sum as a linked 
list
EXAMPLE 
Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
"""
# NOTE: not finished!
from MyLinkedList import LinkedList, Node

def sum_lists(node1, node2, carry):
	print 'sum_lists'

	value = carry
	if node1:
		print "l1 data: ", node1.data
		value = value + node1.data

	if node2:
		print "l1 data: ", node2.data
		value = value + node2.data

	print "value: ", value
	valueDivBy10 = value % 10  # second digit of the number
	resultNode = Node(valueDivBy10)
	print "resultNode.data", resultNode.data



l1 = LinkedList()
l1.insert(3)
l1.insert(7)
l1.insert(9)
# print "size l1: ", l1.get_size()

l2 = LinkedList()
l2.insert(2)
l2.insert(5)
l2.insert(4)
# print "size l2: ", l2.get_size()

sum_lists(l1.head, l2.head, 0)
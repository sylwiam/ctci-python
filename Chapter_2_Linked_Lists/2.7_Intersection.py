""" 
2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inresecting node.
Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the 
second list, then they are intersecting. 

For example, the following two linked lists:

	  A: a1 -> a2 -> c1 -> c2 -> c3
B: b1 -> b2 -> b3 -> c1 -> c2 -> c3

begin to intersect at node c1.

Notes:
* If two linked lists have no intersection at all, return None.
* The linked lists must retain their original structure after the function returns
* You may assume there are no cycles anywhere in the entire linked structure
* Your code should preferably run in O(n) time and use only O(1) memory.
"""

from MyLinkedList import LinkedList, Node

def get_intersection_node(headA, headB):
	# figure out the difference in length of the two linked lists
	# then use that information to traverse the two lists in sync looking out 
	# for when there is an intersection
	# O(n)
	
	listA_length = 0
	listB_length = 0
	
	current_node = headA
	while current_node:  # get size/length of list A
		listA_length = listA_length + 1
		tailA = current_node
		current_node = current_node.next
	
	print "list A tail: ", tailA.data

	current_node = headB
	while current_node:  # get size/length of list B
		listB_length = listB_length + 1
		tailB = current_node
		current_node = current_node.next

	print "list B tail: ", tailB.data

	if tailA.data != tailB.data:
		return None

	if listA_length > listB_length:
		longest = headA
		shorter = headB
	else:
		longest = headB
		shorter = headA
		
	difference = abs(listA_length - listB_length)
	print "difference: ", difference
	
	listA_index = 0
	listB_index = 0
	
	current_node = longest
	while listA_index < difference:
		current_node = current_node.next		
		listA_index = listA_index + 1
	
	intersection = None
	current_other_node = shorter
	while current_other_node:
		if current_other_node == current_node:
			intersection = current_other_node
			break
		
		current_other_node = current_other_node.next
		current_node = current_node.next
	
	return intersection

lA = LinkedList()
lA.insert('c3')
lA.insert('c2')
lA.insert('c1')
lA.insert('a2')
lA.insert('a1')

lB = LinkedList()
lB.insert('c3')
lB.insert('c2')
lB.insert('c1')
lB.insert('b4')
lB.insert('b3')
lB.insert('b2')
lB.insert('b1')

print "list A size: ", lA.get_size()
print "list A head: ", lA.head.data
lA.print_list2(lA.head)

print "list A size: ", lB.get_size()
print "list A head: ", lB.head.data
lA.print_list2(lB.head)

print get_intersection_node(lA.head, lB.head)

# print 'middle', lA.find_middle(lA.head)
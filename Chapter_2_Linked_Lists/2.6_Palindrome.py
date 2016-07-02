""" 
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.

"""

from MyLinkedList import LinkedList, Node

def is_palindrome_iterative(head):
	fast = head
	slow = head
	stack = []
	print "slow: ", slow.data
	print "fast: ", fast.data, '\n'
	
	# Push elements from firt half of linked list onto stack. 
	# When fast runner (which is moving at 2x speed) reaches the end of the linked list,
	# then we know we're at the middle
	while fast is not None and fast.next is not None:
		stack.append(slow.data)
		slow = slow.next
		fast = fast.next.next
		print "slow: ", slow.data
		print "fast: ", fast.data, '\n'
	
	print "slow: ", slow.data
	print "fast: ", fast.data, '\n'
	# has odd number of elements, so skip the middle elemet
	if fast is not None:  
		slow = slow.next

	print "SLOW: ", slow.data

	while slow is not None:
		top = stack.pop()

		if top is not slow.data:
			print 'is NOT palindrome'
			return False

		slow = slow.next

	print 'IS palindrome'
	return True

l1 = LinkedList()
# l1.insert(3)
# l1.insert(7)
# l1.insert(7)
# l1.insert(3)

l1.insert(3)
l1.insert(7)
l1.insert(4)
l1.insert(5)
l1.insert(6)
l1.insert(8)
l1.insert(1)
l1.insert(2)
l1.insert(9)

print "size l1: ", l1.get_size()
print "head: ", l1.head.data
l1.print_list2(l1.head)
is_palindrome_iterative(l1.head)

# print 'middle', l1.find_middle(l1.head)
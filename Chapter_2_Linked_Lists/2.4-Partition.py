"""2.4 Partition: Write code to a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equeal to x. If x is contained within the list, 
the values of only need to be after the elements less than x. The partition element x
can appear anywhere in yhe 'right partition' o, it does not need to appear between the left and the right partitions.
"""

from MyLinkedList import LinkedList, Node


def partition_list(head, x):
	print '--- partition_list ----'
	
	nl = LinkedList(head)  # initialize new list with 1st element form old list
	print "nl size: ", nl.get_size()
	print "head: ", nl.get_head()
	print "tail: ", nl.get_tail()

	current = head
	print "current: ", current.data

	ol_next = current.next
	print "ol_next: ", ol_next.data

	while ol_next != None:
		print
		print "- ol_next: ", ol_next.data
		new_node = Node(ol_next.data)
		if new_node.data < x:
			print '  if'
			new_node.next = nl.head
			nl.head = new_node
			print nl.print_list2(nl.head)
		else:
			print '  else'
			nl.tail.next = new_node
			nl.tail = new_node
			nl.tail.next = None
			print nl.print_list2(nl.head)

		# nl.tail.next = None
		nl.size += 1
		ol_next = ol_next.next

	print "nl size: ", nl.get_size()
	print "nl head data: ", nl.head.data
	print "nl head next: ", nl.head.next.data
	print nl.print_list2(nl.head)


if __name__ == '__main__' :
	ol = LinkedList()
	arr = [4, 25, 12, 3, 2, 10, 5, 1]
	ol.insert_multi(arr)

	print "ol size: ", ol.get_size()
	print ol.print_list()
	print "head: ", ol.get_head()
	print "tail: ", ol.get_tail()
	print partition_list(ol.head, 9)
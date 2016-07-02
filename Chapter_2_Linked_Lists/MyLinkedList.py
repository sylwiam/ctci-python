class Node(object):
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		self.tail = head
		self.size = 0
		if head != None:
			self.size +=1
		

	def insert(self, data):
		new_node = Node(data)
		if self.size == 0:
			self.tail = new_node
			self.tail.next = None
		
		new_node.set_next(self.head)		
		self.head = new_node

		self.size += 1
		# print '----', ' head: ', self.head.data, ' tail: ', self.tail.data

	def insert_multi(self, arr):
		for data in arr:
			self.insert(data)

	def get_head(self):
		if self.head is None:
			return 'empty'
		else:
			return self.head.data

	def get_tail(self):
		if self.tail is None:
			return 'empty'
		else:
			return self.tail.data

	def get_size(self):
		return self.size

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count

	def search(self, data):
		current = self.head
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		return current

	def print_list(self):
		current = self.head  # start traversing from head node

		while current:
			print current.data, '->',
			current = current.get_next()

	def print_list2(self, node):
	    while node:
	        print node.data,'->',
	        node = node.next
	    print


	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	def delete_dups(self):
		""" Remove duplicates from an unsorted linked list
		"""
		all_nodes = {}  # use dictionary to store all nodes while traversing through the linked list
		current = self.head  # start traversing from head node
		all_nodes[current] = True

		while current.next is not None:
			if current.next.data in all_nodes:
				current.next = current.next.next
			else:
				all_nodes[current.next.data] = True
				current = current.next

	def find_middle(self, head):
		fast = head
		slow = head
		mylist = []
		while fast != None and fast.next != None:
			mylist.append(slow.data)
			slow = slow.next
			fast = fast.next.next
		return mylist.pop()

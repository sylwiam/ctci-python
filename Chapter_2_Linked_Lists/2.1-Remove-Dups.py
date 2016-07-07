"""2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from MyLinkedList import LinkedList, Node

ll = LinkedList()

ll.insert('a')
ll.insert('b')
ll.insert('c')
ll.insert('d')
ll.insert('c')
ll.insert('f')
ll.insert('a')
ll.insert('a')

ll.delete_dups()

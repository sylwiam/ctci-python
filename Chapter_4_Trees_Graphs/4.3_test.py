from MyLinkedList import LinkedList, Node

class TreeNode:

      def __init__(self,info): #constructor of class

          self.info = info  #information for node
          self.left = None  #left leef
          self.right = None #right leef
          self.level = None #level none defined

      def __str__(self):

          return str(self.info) #return as string


class SearchTree:

      def __init__(self): #constructor of class

          self.root = None


      def create(self,val):  #create binary search tree nodes
          if self.root == None:
             self.root = TreeNode(val)
          else:
             current = self.root
             while 1:
                 if val < current.info:
                   if current.left:
                      current = current.left
                   else:
                      current.left = TreeNode(val)
                      break;      
                 elif val > current.info:            
                    if current.right:
                       current = current.right
                    else:
                       current.right = TreeNode(val)
                       break;      
                 else:
                    break 

      def bft(self): #Breadth-First Traversal
          self.root.level = 0 
          queue = [self.root]
          out = []
          current_level = self.root.level

          while len(queue) > 0: 
             current_node = queue.pop(0)
 
             if current_node.level > current_level:
                current_level += 1
                out.append("\n")

             out.append(str(current_node.info) + " ")

             if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                  
             if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
                 
          print "".join(out)   


      def bft_2(self): #Breadth-First Traversal
          queue = [self.root]
          levels = {}
          current_level = 0
          while len(queue) > 0: 
             current_level
             current_node = queue.pop(0)
             
             if current_node.level > current_level:
                current_level += 1

             # print "level: ", current_level
             # print "node: ", current_node.info 

             print levels
             if current_level not in levels.keys():
                 levels[current_level] = [current_node.info]
             else:
                 item = levels[current_level]
                 item.append(current_node.info)

             if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                  
             if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
                 
          # print "".join(out) 
          print levels
          return levels

      def inorder(self,node):            
           if node is not None:
              
              self.inorder(node.left)
              print node.info
              self.inorder(node.right)


      def preorder(self,node):        
           if node is not None:
              
              print node.info
              self.preorder(node.left)
              self.preorder(node.right)


      def postorder(self,node):            
           if node is not None:
              
              self.postorder(node.left)
              self.postorder(node.right)
              print node.info

                          
tree = SearchTree()     
arr = [8,3,1,6,4,7,10,14,13]
for i in arr:
    tree.create(i)
print 'Breadth-First Traversal'
lists_dict = tree.bft_2()

for value in lists_dict.values():
    print 'value: ', value
    linkedlist = LinkedList()
    for item in value:
        linkedlist.insert(item)
    
    linkedlist.print_list2(s)
    # print linkedlist
# print 'Inorder Traversal'
# tree.inorder(tree.root) 
# print 'Preorder Traversal'
# tree.preorder(tree.root) 
# print 'Postorder Traversal'
# tree.postorder(tree.root) 
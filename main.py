# class Node:
#     #constructor
#     def __init__(self, data, next):
#         self.data = data
#         self.next = next
#     #tell python how to print this node
#     def __str__(self):
#         return str(self.data)

# # myNode = Node('taylor', None)
# # romeNode = Node('Rome', myNode)

# # myNode.next = romeNode

# # print(romeNode.next)
# # print(myNode.next)

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     #retruns length of the list
#     def __len__(self):
#         return self.size

#     def __str__(self):
#         if self.size == 0:
#             return '[]'
#         current = self.head
#         # what we return once we have concantenated
#         result = str(current)
#         while current.next:
#             result += f' -> {str(current.next)}'
#             current = current.next
#         return f'[{result}]'


# # insert a new Node at the front of the list
#     def insert_front(self, data):
#         if self.size == 0:
#             # create a new node and make it the head
#             self.head = Node(data, None)
#             # also set the tail to the same node
#             self.tail = self.head
#         elif self.size == 1:
#             self.head = Node(data, self.tail)
#         else:
#             temp = self.head
#             self.head = Node(data, temp)
#         self.size +=1

#     def insert_end(self, data):
#         if self.size == 0:
#             self.head = Node(data, None)
#             self.tail = self.head
#         elif self.size == 1:
#             self.tail = Node(data, None)
#             self.head.next = self.tail
#         else :
#             temp = self.tail
#             self.tail = Node(data, None) 
#             temp.next = self.tail
#         self.size += 1   

#     def insert_after(self, data, node_data):
#         temp = None
#         # make sure the person exists
#         current = self.head
#         while current.next:
#             # found Pete
#             if current.data == node_data:
#                 temp = current
#                 break
#             current = current.next
#         # Pete was nowhere to be found    
#         if temp == None:
#             return 'check your node_data, we couldn\'t find him!'
#         # create the new node and poit it at Adam, the person after pete
#         newNode = Node(data, temp.next)
#         # set Person.next to the new Node
#         temp.next = newNode
#         self.size += 1
        


# myList = LinkedList()
# myList.insert_front('Adam')
# myList.insert_front('Pete')
# myList.insert_front('Pete')
# myList.insert_front('Yoel')
# myList.insert_end('Philip')
# myList.insert_after('Rome', 'Pete')
# print(myList)
# print(len(myList))

def queue_time(customers, n):
    tills = [0]*n
    for i in customers:
      tills[0] += i
      tills.sort()
    return max(tills)
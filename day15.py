"""
Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument)
and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, 
return the reference to the  head node.

Note: If the head argument passed to the insert function is null, then the initial list is empty.

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        node = Node(data)
        if head is None:
            head = node
        else:
            current = head
            while current:
                if current.next is None:
                    current.next = node
                    break 
                else:
                    current = current.next

        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
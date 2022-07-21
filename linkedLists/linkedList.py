from locale import currency
from os import access

from requests import head


class Node:

    def __init__(self,data):
            self.data = data
            self.next_node = None

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def returnSize(self):
        return self.size

# O(1) - constant
    def insertAtStart(self,data):
        self.size +=1 
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node

        else:
            new_node.next_node = self.head
            self.head = new_node

    def insertAtEnd(self,data):
        self.size +=1 
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            currentNode = self.head
            while currentNode.next_node is not None:
                currentNode = currentNode.next_node

            currentNode.next_node  = new_node    
                   
    def traverse(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode)
            currentNode = currentNode.next_node
        

    def remove(self, data):
        if(self.head is None) : return

        currentNode = self.head
        prevNode = None

        # set prev and current node pointers
        while currentNode.next_node is not None and currentNode.data!=data:
            prevNode = currentNode
            currentNode = currentNode.next_node

        if currentNode is None:
            return    

        # if youre removing head
        if(prevNode is None):
            self.head = currentNode.next_node
            self.size -= 1
        else:
            prevNode.next_node = currentNode.next_node
            self.size -= 1    

    def removeAtStart(self):
        if(self.size==0):
            return
        currentNode = self.head
        self.head = currentNode.next_node
        self.size -=1 

    def removeAtPos(self, pos):
        if (pos> self.size-1  or self.size ==0 ):
            return

        if(pos==0):
            self.removeAtStart()
            return    

        i = 0 

        prevNode = None
        currentNode = self.head
        
        while i != pos:
            prevNode = currentNode
            currentNode = currentNode.next_node
            i+=1
        
        prevNode.next_node = currentNode.next_node
        self.size -= 1   

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtStart(1)
    ll.insertAtEnd(2)
    ll.insertAtEnd(3)
    ll.insertAtEnd(4)
    ll.insertAtEnd(5)
    ll.insertAtEnd(6)
    ll.traverse()

     
         
    
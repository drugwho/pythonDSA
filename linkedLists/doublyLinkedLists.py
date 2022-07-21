class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    
    def insertAtStart(self, data):
        newNode = Node(data)
        
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode.nextNode = self.head
            self.head.prevNode = newNode
            self.head = newNode
            self.size += 1
    

    def insertAtEnd(self, data):
        newNode = Node(data)
        
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode.prevNode = self.tail
            self.tail.nextNode = newNode
            self.tail = newNode
            self.size += 1

    def traverseFromStart(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next_node

    def traverseFromEnd(self):
        currentNode = self.tail
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.prevNode


if __name__ == "__main__":

    dl = DoubleLinkedList()

    dl.insertAtEnd(1)
    dl.insertAtEnd(2)
    dl.insertAtEnd(3)
    dl.insertAtStart(0)
    dl.traverseFromEnd()


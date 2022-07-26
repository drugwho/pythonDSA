class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        # important to store parent in removal
        self.parent = parent


"""
storage : O(N)
search, del, insert : best O(logN) (balanced), 
                    worst O(N) (imbalanced - right and left have different heights,
                    resembles linked lists, if a sorted array is fed into the BST)

predecessor : largest item in left subTree
sucessor: smallest item in right subTree

pre-order: root - left subTree - right subTree
post-order: left subTree - right subTree -  root
in-order:  left subTree - root - right subTree // yields sorted order

"""


class BST:
    def __init__(self) -> None:
        # we can access only root, all other nodes are accessed via root
        self.rootNode = None
        self.size = 0

    def insertNode(self, data, node):
        # recurse through the tree, insert in left
        # or right based on the val of data
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node=node.leftChild)
            else:
                node.leftChild = Node(data)
                node.leftChild.parent = node
                self.size += 1
        else:
            if node.rightChild:
                self.insertNode(data, node=node.rightChild)
            else:
                node.rightChild = Node(data)
                node.rightChild.parent = node
                self.size += 1

    def insert(self, data):
        if self.rootNode is None:
            self.rootNode = Node(data)
            self.size += 1
        else:
            self.insertNode(data=data, node=self.rootNode)

    def getSize(self):
        return self.size

    def getMin(self):
        if self.rootNode is None:
            return
        else:
            currentMin = self.rootNode
            while currentMin.leftChild:
                currentMin = currentMin.leftChild
            return currentMin.data

    def getMax(self):
        if self.rootNode is None:
            return
        else:
            currentMax = self.rootNode
            while currentMax.rightChild:
                currentMax = currentMax.rightChild
            return currentMax.data

    def traverse(self, type):
        if type.lower() == "in":
            if self.rootNode:
                self.inOrder(self.rootNode)
        elif type.lower() == "pre":
            if self.rootNode:
                self.preOrder(self.rootNode)
        elif type.lower() == "post":
            if self.rootNode:
                self.postOrder(self.rootNode)

    def postOrder(self, node):
        if node.leftChild:
            self.preOrder(node.leftChild)

        if node.rightChild:
            self.preOrder(node.rightChild)
        print(node.data)

    def preOrder(self, node):
        print(node.data)

        if node.leftChild:
            self.preOrder(node.leftChild)

        if node.rightChild:
            self.preOrder(node.rightChild)

    def inOrder(self, node):
        if node.leftChild:
            self.inOrder(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.inOrder(node.rightChild)

    def remove(self, data):
        if self.rootNode:
            self.removeNode(data, self.rootNode)


    def removeNode(self, data, node):
        # find node we want to remove
        if node is None:
            return

        if data < node.data:
            self.removeNode(data, node.leftChild)
        elif data > node.data:
            self.removeNode(data, node.rightChild)
        else:
            # we found the node to remove
            # Case 1 : Leaf Node check

            if node.leftChild is None and node.rightChild is None:
                print("Removing Leaf Node ... %d" % node.data)
                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.rootNode = None

                del node   

            # Case 2: Node has 1 child

            elif(node.leftChild is None and node.rightChild is not None):
                print("Removing a node with single rightChild")

                parent = node.parent

                if(parent is not None and parent.leftChild ==node):
                      parent.leftChild = node.rightChild
                      
                if(parent is not None and parent.rightChild ==node):
                      parent.rightChild = node.rightChild

                
                if parent is None:
                    self.rootNode = node.rightChild

                node.rightChild.parent = parent    
          
            elif(node.rightChild is None and node.leftChild is not None):
                print("Removing a node with single leftChild")

                parent = node.parent

                if(parent is not None and parent.leftChild ==node):
                      parent.leftChild = node.leftChild
                      
                if(parent is not None and parent.rightChild ==node):
                      parent.rightChild = node.leftChild

                
                if parent is None:
                    self.rootNode = node.leftChild

                node.leftChild.parent = parent    
          
            # Case 3: Remove node with 2 children:
                # find predecessor and swap with root node 
                #  then remove the root node (since it is a leaf)
            
            else:
                print("removing a node with 2 children")
                predecessor = self.getPredecessor(node.leftChild)

                # swap with predecessor
                print("swapping with predecessor")
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.removeNode(data, predecessor)

    def getPredecessor(self, node):
        if node.rightChild:
                return self.getPredecessor(node.rightChild)

        return node

if __name__ == "__main__":
    bst = BST()

    bst.insert(10)
    bst.insert(1)
    bst.insert(100)
    bst.insert(-10)

    print("\n")
    print("******************")
    bst.traverse("in")

    bst.remove(10)

    print("******************")
    bst.traverse("in")
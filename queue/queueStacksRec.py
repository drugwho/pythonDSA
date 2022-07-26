class Queue:
    def __init__(self):
        self.queueStack = []

    def enqueue(self, data):
        self.queueStack.append(data)

    def dequeue(self):
        if(len(self.queueStack)==0):
            raise Exception("Stacks are empty")

        if(len(self.queueStack))==1:
            return self.queueStack.pop()


        item = self.queueStack.pop()
        
        
        deqItem = self.dequeue()

        self.queueStack.append(item)

        return deqItem

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    a =q.dequeue()

    print(a)
        
        
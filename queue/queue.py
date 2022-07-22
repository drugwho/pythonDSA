class Queue:
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return True if len(self.queue) == 0 else False

    def size(self):
        return len(self.queue)

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if(self.isEmpty()):
            return
        element = self.queue[0]
        del self.queue[0]          
        return element

    def peek(self):
        if(self.isEmpty()):
            return  
        return self.queue[0] 

    def printQueue(self):
        print(self.queue)    


if __name__ == "__main__":
    qu = Queue()
    print(qu.isEmpty())
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)


    print(qu.peek())
    qu.printQueue()

    print(qu.isEmpty())
    qu.dequeue()
    qu.printQueue()
    qu.dequeue()
    qu.dequeue()

    qu.printQueue()
class Queue:
    def __init__(self):
        self.enqueueStack = []
        self.dequeueStack = []

    def enqueue(self, data):
        self.enqueueStack.append(data)

    def dequeue(self):
        if(len(self.enqueueStack)==0 and len(self.dequeueStack)==0):
            raise Exception("Stacks are empty")

        if(len(self.dequeueStack)==0):
            while not len(self.enqueueStack)==0:
                self.dequeueStack.append(self.enqueueStack.pop())
        return self.dequeueStack.pop()
        

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())

class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return True if len(self.stack) == 0 else False

    def size(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if(self.isEmpty()):
            return
        element = self.stack[-1]
        del self.stack[-1]          
        return element

    def peek(self):
        if(self.isEmpty()):
            return  
        return self.stack[-1] 

    def printStack(self):
        print(self.stack)    


if __name__ == "__main__":
    st = Stack()
    print(st.isEmpty())
    st.push(1)
    st.push(2)
    st.push(3)

    print(st.peek())
    print(st.isEmpty())
    st.printStack()
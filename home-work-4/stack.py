class MyStack:
    def __init__(self):
        self.size =  10
        self.stack = [None] * self.size
        self.isEmpty = True
        self.isFull = False
        self.current = 0
    
    def push( self, newElement: int | str | dict | list):
        self.stack[self.current] = newElement
        self.current+=1
        self.isFull = self.current == self.size
        self.isEmpty = self.current == 0
    
    def pop(self):
        if self.isEmpty:
            return "Stack is empty"
        popIndex = self.current - 1
        popElement = self.stack[popIndex]
        self.stack[popIndex] = None
        self.current-=1
        self.isFull = self.current == self.size
        self.isEmpty = self.current == 0
        return popElement    
        




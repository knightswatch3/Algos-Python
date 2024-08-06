
from stack import MyStack

def stackSorter(inputStack: MyStack):
    bufferStack = MyStack()
    bufferVal = inputStack.pop()

    while bufferVal != 'Stack is empty':
        if bufferStack.isEmpty:
            bufferStack.push(bufferVal)
        else:
            bufferCounter = 0
            if str(bufferVal) != 'Stack is empty' and bufferStack.stack[bufferStack.current - 1] > bufferVal:
                while not bufferStack.isEmpty and bufferStack.stack[bufferStack.current-1] > bufferVal:
                    inputStack.push(bufferStack.pop())
                    bufferCounter+=1
                bufferStack.push(bufferVal)
                while bufferCounter !=0:
                    bufferStack.push(inputStack.pop())
                    bufferCounter-=1
            else:
                bufferStack.push(bufferVal)
        bufferVal = inputStack.pop()
        
    return bufferStack.stack

checker = MyStack()
checker.push(6)
checker.push(15)
checker.push(1)
checker.push(20) 
checker.push(9)
print(stackSorter(checker))
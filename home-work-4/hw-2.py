from stack import MyStack


def postFix_Infix(inputString: str):
    buffer = MyStack()
    finalVal = 0
    arithmeticChars = ['+','-','*','/']
    for character in inputString:
        if character in arithmeticChars:
            # perform the operation
            operationToPerform = character + buffer.pop()
            finalVal = eval(buffer.pop() + operationToPerform)
            buffer.push(str(finalVal))
            print("finalVal is", finalVal)
        else:
            buffer.push(character)
    return buffer.pop()


postfixString = "84/"
print(postFix_Infix(postfixString))
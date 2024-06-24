# Given a number n and another number n1. Print only the first n1 factors of n.

def firstNFactors(inputNum: int, count:int):
    if(count>inputNum):
        print("Given count of factors cannot be greater than input number")
        return
    else:
        # factors = [i for i in range(1, count+1) if inputNum%i==0]
        i=1
        res=[]
        while count>0 and i<inputNum:
            if inputNum%i==0:
                res.append(i)   
                count-=1
            i+=1
        return res

print(firstNFactors(20,3))


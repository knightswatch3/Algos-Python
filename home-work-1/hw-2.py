# Take 2 numbers n1 and n2. Print that the numbers are good numbers if there is NO existence of a number between them which is divisible by 13. If they are not good numbers then print they are awesome numbers if the sum of the odd numbers between them is divisible by 5. If neither of the conditions is met then print that these numbers are normal numbers

# What did I look for ? 
# 1. function arg default types() -> I guessed somthing like this would exist and trial and error worked as it works in javascript
def hw2(numeric1: int, numeric2: int):
    gNums = [i for i in range(numeric1, numeric2+1) if i%13==0]
    if(len(gNums))==0:
        print('Numbers are good numbers')
        return
    else: 
        aNums = [i for i in range(numeric1, numeric2+1) if i%2!=0]
        if(sum(aNums)%5==0):
            print('Numbers are awesome numbers', aNums)
            return
    print("These are normal numbers")
    

        

hw2(10,15)
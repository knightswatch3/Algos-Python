# Palindrome
def reverse(input: int):
    rev=0
    while(input>0): 
        rev=int((rev*10)+(input%10))
        input=int(input/10)
    return rev

def palin(input:int):
    return input==reverse(input)

print(palin(101))

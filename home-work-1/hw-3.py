# Find whether a number is Narcissist or not
# What did I look for ? 
# 1. pow function() -> I guessed somthing like this would exist and trial and error worked as it worked in javascript
def narc_check(input: int):
    power=len(str(input))
    sum=0
    for i in range(0,power):
        sum += pow(int(str(input)[i]),power)
    return sum==input

print(narc_check(153))


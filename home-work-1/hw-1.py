# 1. Take 2 numbers and keep subtracting the smaller number from the higher till they both become equal.

# For example:
# If n1 is 10 and n2 is 15 then the updating of those numbers should be as follows

# n1       n2 
# ----------------
# 10.       15
# 10.        5
# 5.         5

def executor(numeric1: int, numeric2: int):
    print('\nNumeric1:', numeric1)
    print('\nNumeric2:', numeric2)
    if(numeric1>numeric2):
        numeric1,numeric2=numeric2,numeric1
    if(numeric1==numeric2):
        print('Numbers are same', numeric1, ' == ', numeric2)
        return
    numeric2 = numeric2-numeric1
    executor(numeric1, numeric2)

executor(20,25)
    




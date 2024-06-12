import math
    # Find list whose sum is the most
def maxSum(lisOflis: list[list[int]]):
    # Approach-1 I can fetch the sum of the list and map it to the index and return the index with max sum
    # Approach-2 Googled the max function definition and found that I can use something called a key
    return max(lisOflis, key=lambda lst: max(lst))

print(maxSum([
    [1,2,3],
    [7,0,1],
    [0,3,9]
]))


   # Find list whose first and last numbers are same
def sameNum(lisOflis: list[list[int]]):
    # Approach-1 I can fetch the sum of the list and map it to the index and return the index with max sum
    # Approach-2 Googled the max function definition and found that I can use something called a key
        # numberCheck = lambda lst: lst[0]==lst[len(lst)-1]
        # newList = [lst for lst in lisOflis if numberCheck(lst)]
        # return newList
    return [lst for lst in lisOflis if lst[0]==lst[len(lst)-1]]

print(sameNum([
    [1,2,1],
    [7,0,1],
    [0,3,9]
]))

# Get a list of sums of the last 3 numbers of each list in one line 
def lastthree(lisOflis: list[list[int]]):
    return [sum(lst[-3:]) for lst in lisOflis]

print(lastthree([[1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50, 60],
    [7, 14, 21, 28, 35, 42, 49],
    [100, 200, 300, 400, 500, 600, 700, 800],
    [5, 10, 15, 20, 25],
    [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],
    [0, 1, 4, 9, 16, 25, 36, 49, 64],
    [3, 6, 9, 12, 15],
    [8, 16, 24, 32, 40, 48],
    [2, 4, 6, 8, 10, 12, 14]
]))

# Get a list of sum of odd values in each list 
def oddsum(lisOflis: list[list[int]]):
    return [sum(lst[1::2]) for lst in lisOflis]

print(oddsum([[1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50, 60],
    [7, 14, 21, 28, 35, 42, 49],
    [100, 200, 300, 400, 500, 600, 700, 800],
    [5, 10, 15, 20, 25],
    [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],
    [0, 1, 4, 9, 16, 25, 36, 49, 64],
    [3, 6, 9, 12, 15],
    [8, 16, 24, 32, 40, 48],
    [2, 4, 6, 8, 10, 12, 14]
]))
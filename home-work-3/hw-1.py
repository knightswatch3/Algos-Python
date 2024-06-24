#  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def dupCheck(inputLst: list[int]) -> bool:
    buffer = {}
    for i in inputLst:
        if i in buffer.keys():
            return True
        else:
            buffer[i]=1
    return False


print(dupCheck([1, 2, 3, 4, 5, 6, 2]))  # Output: True
print(dupCheck([1, 2, 3, 4, 5, 6]))  # Output: False
print(dupCheck([7, 7, 7, 7, 7]))  # Output: True
print(dupCheck([-1, -2, -3, -4, -1]))  # Output: True
print(dupCheck([]))  # Output: False
print(dupCheck([10]))  # Output: False
print(dupCheck([1, 1, 2, 3, 4, 4, 5, 6, 6]))  # Output: True
print(dupCheck([999999999, 888888888, 777777777]))  # Output: False
print(dupCheck([1, 'a', 3.0, 1]))  # Output: True (but should avoid mixed types)
print(dupCheck([0, 1, 2, 0]))  # Output: True
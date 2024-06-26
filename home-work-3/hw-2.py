# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    # Example 1:
        # Input: strs = ["eat","tea","tan","ate","nat","bat"]
        # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    # Example 2:
        # Input: strs = [""]
        # Output: [[""]]
    # Example 3:
        # Input: strs = ["a"]
        # Output: [["a"]]
# Time complexity of this block is O(m)+O(n)
def anaChecker(input1: str, input2: str):
    input1Dict=input2Dict={}
    for character1 in input1:
        if character1 in input1Dict.keys():
            input1Dict[character1]+=1
        else:
            input1Dict[character1]=1
    for character2 in input2:
        if character2 in input1Dict:
            input1Dict[character2]-=1
        else:
            return False
    for value in input1Dict.values():
        if value!=0:
            return False
    return True

def anagrouper(inputLst: list[str]):
    buffer = set()
    if len(inputLst)==1:
        return list([inputLst])
    else:
        finalList=[]
        for idx,element in enumerate(inputLst):
            if element not in buffer:
                subList=[element]
                buffer.add(element)
                for remaining in inputLst[idx+1:]:
                    if remaining not in buffer and anaChecker(element, remaining):
                        subList.append(remaining)
                        buffer.add(remaining)
                finalList.append(subList)
        return finalList
        




def optimizedAnaGrouper(inputList):
    buffer = {}
    for element in inputList:
        sortWord = ''.join(sorted(element))
        if sortWord not in buffer:
            buffer[sortWord]=[]
        buffer[sortWord].append(element)
    return list(buffer.values())




print(optimizedAnaGrouper(["eat","tea","tan","ate","nat","bat"]))
print(optimizedAnaGrouper([""]))
print(optimizedAnaGrouper(["a"]))
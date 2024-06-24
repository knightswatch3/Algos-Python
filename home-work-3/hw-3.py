# . Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such as a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

def patternChecker(pattern: str, inputString: str):
    patternList = list(pattern)
    inputList = inputString.split(" ")
    if(len(set(patternList))!=len(set(inputList))):
        return False
    patternDict = inputDict = {}
    for idx,patternChar in enumerate(patternList):
        if patternChar in patternDict.keys():
            patternDict[patternChar]+=str(idx)
        else:
            patternDict[patternChar]=str(idx)
    for idx,subString in enumerate(inputList):
        if subString in inputDict.keys():
            inputDict[subString]+=str(idx)
        else:
            inputDict[subString]=str(idx) 
    for i in range(len(patternList)-1): 
        if(patternDict[patternList[i]]!=inputDict[inputList[i]]):
            return False
    return True





print(patternChecker("abba","dog cat cat dog"))
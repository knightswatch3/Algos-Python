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
    patternList = list(pattern) # splitting pattern into list
    inputList = inputString.split(" ") # splitting input string into words to match pattern 
    if(len(set(patternList))!=len(set(inputList))): # if lengths are unequal then return false as pattern fails to match
        return False
    patternDict ,inputDict = {},{} # create dictonaries for each 
    for idx,patternChar in enumerate(patternList): # map the indieces of the character (in pattern array) to the dictionary as a string
        if patternChar in patternDict.keys():
            patternDict[patternChar]+=str(idx)
        else:
            patternDict[patternChar]=str(idx)
    for idx,subString in enumerate(inputList): # map the indieces of the character (in pattern array) to the dictionary as a string
        if subString in inputDict.keys():
            inputDict[subString]+=str(idx)
        else:
            inputDict[subString]=str(idx) 
    for i in range(len(patternList)-1):  # iterate through either of the list (pattern list or input string list) to ensure the pattern strings of indieces match. If they don't quit and return false
        if(patternDict[patternList[i]]!=inputDict[inputList[i]]):
            return False
    return True





print(patternChecker("abba","dog cat cat dog"))
print(patternChecker("aaaa","dog cat cat dog"))
print(patternChecker("abba","dog cat cat fish"))

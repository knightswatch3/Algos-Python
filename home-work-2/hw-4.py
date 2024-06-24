# Given a list of list of words, perform the following operations 

def charCount(inputWord: str):
    mydict = {}
    for char in inputWord:
        if(char in mydict.keys()):
            mydict[char]+= 1
        else:
            mydict[char]= 1
    print(mydict)

charCount("batman")

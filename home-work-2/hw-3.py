# Given a list of list of words, perform the following operations 

def firstandLast(lisOflis: list[list[str]]):
    return [lst for lst in lisOflis if lst[0]==lst[len(lst)-1]]

list_of_words = [
    ["apple", "banana", "cherry", "apple"],
    ["dog", "cat", "fish", "bird"],
    ["hello", "world", "hello"],
    ["python", "java", "c++", "python"],
    ["start", "middle", "end"],
    ["repeat", "this", "repeat"],
    ["same", "words", "same"],
    ["front", "center", "back", "front"],
    ["unique", "words", "list"],
    ["loop", "over", "loop"]
]


print(firstandLast(list_of_words))


newListofWords = [["book"], ["trees","bat","good"],["ok","bye"]]

def threebsolution(lisOflis: list[list[str]]):
    oddsum = lambda lst, count=0: len(''.join([element for element in lst if len(element)%2!=0]))
    return [tuple([len(''.join(lst)), oddsum(lst)] ) for lst in lisOflis]

print(threebsolution(newListofWords))

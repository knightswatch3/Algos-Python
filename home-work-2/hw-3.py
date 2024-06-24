# Given a list of list of words, perform the following operations 

def firstandLast(lisOflis: list[list[str]]):
    return sum([len([word for word in lst if word[0]==word[len(word)-1]]) for lst in lisOflis])

list_of_words = [
    ["satis", "banana", "cherry", "satis"],
    ["dog", "cat", "fish", "bird"],
    ["zazz", "world", "hello"],
    ["python", "aira", "c++", "python"],
    ["start", "middle", "end"],
    ["madam", "this", "madam"],
    ["same", "words", "same"],
    ["front", "center", "back", "front"],
    ["unique", "words", "list"],
    ["loop", "over", "loop"]
]


print(firstandLast(list_of_words))


newListofWords = [["book"], ["trees","bat","good"],["ok","bye"]]

def threebsolution(lisOflis: list[list[str]]):
    oddsum = lambda lst: len(''.join([element for element in lst if len(element)%2!=0]))
    return [tuple([len(''.join(lst)), oddsum(lst)] ) for lst in lisOflis]

print(threebsolution(newListofWords))

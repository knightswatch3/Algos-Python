
# Printing even multiples of a given number
def alpha():
    numeric = int(input("Enter a number: "))
    result = []
    for i in range(1,101):
        if(i>=numeric and i%numeric ==0 and i%2 ==0):
            result.append(i)
    print(result)


def alpha2():
    numeric = int(input("Enter a number: "))
    result = [i for i in range(1,101) if i>=numeric and i%numeric ==0 and i%2 ==0]
    print(result)
# alpha()

# List comprehension example
result = [i*10 for i in range(1,21)]
print("\nif comprehension: ", result)

result_1 = [i*10 if i%3==0 else i*5 for i in range(1,21)]
print("\nif else comprehension: ", result_1)

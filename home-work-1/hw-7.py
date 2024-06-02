# Take 2 numbers and find how many digits are common in both the numbers
# What did I look for ? 
# How to check existence of an element in python set
def common(numeric1:int, numeric2:int):
    list1 = [int(str(numeric1)[i]) for i in range(0,len(str(numeric1)))]
    list2 = [int(str(numeric2)[i]) for i in range(0,len(str(numeric2)))]
    uniq_list1=set(list1)
    uniq_list2=set(list2)
    commonCount=0
    for i in uniq_list1:
        if i in uniq_list2:
            commonCount+=1
    return commonCount

print(common(123,2334))
 
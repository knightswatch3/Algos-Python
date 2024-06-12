def common(numeric1:int, numeric2:int):
    list1 = [int(str(numeric1)[i]) for i in range(0,len(str(numeric1)))] #O(n)
    list2 = [int(str(numeric2)[i]) for i in range(0,len(str(numeric2)))] #O(m)
    uniq_list1=set(list1) # O(n) for iteration over list + O(n) * O(1) for each element to be inserted = O(n)
    uniq_list2=set(list2) # O(m) for iteration over list + O(m) * O(1) for each element to be inserted = O(m)
    commonCount=0
    for i in uniq_list1: # O(n) for iteration of the unique list 1
        if i in uniq_list2:  # O(m) for iteration of the unique list 2
            commonCount+=1
    return commonCount

# Final time complexity of the function is => O(n) + O(m) 
# Take a number and store the reversed number in a new variable. The skeleton of the code is given below 

# int num = <Input provided>
# int reverse = 0;

# while( num > 0) {

#  int dig = ______;
#  reverse = _____ * _____ + _____;
#  num = num /10;

# }

def reverse(input: int):
    rev=0
    while(input>0):
        print('Input is', input)
        rev=int((rev*10)+(input%10))
        input=int(input/10)
    print("Reverse is", rev)

reverse(103)

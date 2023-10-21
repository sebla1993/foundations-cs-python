#number1
def getfactorial():
    y = 1
    x = int(input("put an integer"))
    if x<0:
         print("sorry factorial does not exist for negative numbers")
    elif x==0:
        print("the factorial of 0 is 1")
    else:
        for i in range(1, x+1):
            y=y*i
    return("the factorial of",x, "is", y)
print(getfactorial())
#number2

def devisor():
    y = []
    x = int(input("put an integer number"))
    for i in range(1, x+1):
      if x % i == 0:
        y.append(i)
    print(y)

devisor()
#number3
def reverseString():
    x = str(input("write what do you want"))
    y = ""
    for i in x:
      y = i + y
    print(y)
reverseString()
#number4

    string_array = input("put your numbers here ").split(',')
    y = [int(numeric_string) for numeric_string in string_array]
    result = []
    for number in y:
        if number % 2 == 0:
            result.append(number)
    print(result)


def even_number2(input_data):
    string_array = input_data.split(',')
    y = [int(numeric_string) for numeric_string in string_array]
    result = []
    for number in y:
        if number % 2 == 0:
            result.append(number)
    print(result)

#number5
cap_found = 0
if len(password) < 8:
    print("weak password")
    return

all_cap = ['A', 'B' 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for cap in all_cap:
    for letter in password:
        if letter == cap:
            cap_found = 1
            break
if cap_found == 0:
    print("weak password")

def check_pass(password):     return

    all_cap = ['a', 'b', 'c']

    for cap in all_cap:
        for letter in password:
            if letter == cap:
                cap_found = 1
                break
    if cap_found == 0:
        print("weak password")
        return

    all_cap = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']
    for cap in all_cap:
        for letter in password:
            if letter == cap:
                cap_found = 1
                break
    if cap_found == 0:
        print("weak password")
        return

    for letter in password:
        if letter.isdigit():
            cap_found = 1
            break
    if cap_found == 0:
        print("weak password")
        return
    print("strong password")
x = input("what is your password?")
check_pass(x)


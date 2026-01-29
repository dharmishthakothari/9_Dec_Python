from functools import reduce
def add(num1,num2):
    return num1+num2

def mul(num1,num2):
    return num1*num2
ans=reduce(mul,[1,2,3,4,40,56])
print(ans)
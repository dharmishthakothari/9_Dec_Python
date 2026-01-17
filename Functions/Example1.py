# function with no paramter no return 
def greet():
    print("Have a good day")

#function with single paramter no return 
def greet1(name):
    print("Have a good day ",name)

# function with 2 paramters and return value 
# pass 2 values and return sum 

def add(no1,no2):
    ans=no1+no2
    return ans

greet()
greet()
greet()
greet1("Ami")
greet1("Priyanshu")
greet1("Abhijit")
ans=add(23,11)
print(f"Sum is {ans}")

ans=add(23,113434)
print(f"Sum is {ans}")
def sq(no):
    return no*no

def isEven(no):
    return no%2==0

number=int(input("Enter number "))

#ans=sq(number)
#print(f"The square of {number} is {ans}")

print(f"The {number} is {isEven(number)}")

#find square if number is even 

if isEven(number):
    print(f"The square of {number} is {sq(number)}")


def factororial(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    return fact
def checkEven(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
while True:
    print("1. Factorial")
    print("2. Even/Odd")
    print("3. Palidrome")
    print("4. Exit")
    choice=int(input("Enter choice "))
    number=int(input("Enter number "))
    match(choice):
        case 1:
            ans=factororial(number)
            print(f"Factorial of {number} is {ans}")
        case 2: 
            ans=checkEven(number)
            print(f"{number} is {ans}")
        case 4: break
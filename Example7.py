number1=int(input("Enter number 1 "))
number2=int(input("Enter number 2 "))

# check number1 greater number2 and also check number1 is greater 100
print(f"AND {number1>number2 and number1>100}")
print(f"OR {number1>number2 or number1>100}")
print(f"not in OR {not(number1>number2 or number1>100)}")
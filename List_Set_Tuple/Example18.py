num1 = {1,2,4,3}
num2={22,33,44,2,4,55}
num4={1,2,44}
# num3=num1.intersection(num2,num4)
# num3=num1&num2&num4
#Union 
# num3=num1.union(num2,num4)
num3=num1|num2|num4
print(num3)

num3=num2.difference(num1)
print(f"Difference {num3}")


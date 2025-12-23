
num= int(input("Enter number "))
temp=1
for i in range(2,num):
    if num%i ==0:
        temp=1
        print("Not a prime")
        break
    else:
        temp=0
        
if temp==0:
    print("number is prime")
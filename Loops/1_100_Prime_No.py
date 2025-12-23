# Online Python compiler (interpreter) to run Python online.num=

for num in range(3,101):
    temp=1
    for i in range(2,num):
        if num%i ==0:
            temp=1
            print(f"{num} is not prime")
            break
        else:
            temp=0
    if temp==0:
        print(f"{num} is prime")
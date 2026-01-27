def checkEven(num):
    if num%2==0:
        return num
    
lst_numbers = [2,3,4,6,7,9]
lst_ans=list(filter(checkEven,lst_numbers))
print(lst_ans)

lst_ans1=list(map(checkEven,lst_numbers))
print(lst_ans1)

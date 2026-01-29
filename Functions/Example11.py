# numbers are even then find square 
def checkEven(num):
    if num%2==0:
        return num
def sq(num):
    return num*num

lst_numbers=[1,2,3,4,5,6]
# [4,16,36]
# lst_even=list(filter(checkEven,lst_numbers))

# lst_ans=list(map(sq,lst_even))
# print(lst_ans)

#Single line 
lst_ans=list(map(sq,list(filter(checkEven,lst_numbers))))
print(lst_ans)
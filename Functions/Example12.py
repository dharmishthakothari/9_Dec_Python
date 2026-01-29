    
lst_numbers = [2,3,4,6,7,9,34,55,67,89,90]
lst_ans=list(filter(lambda num:num%2==0,lst_numbers))
print(lst_ans)

lst=list(map(lambda num:num*num,lst_ans))
print(lst)
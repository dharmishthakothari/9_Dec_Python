# add int values from list 
lst_numbers = [1,'sneha',2,6,4,200,44.70]
sum=0
for i in lst_numbers:
    #print(i)
    if type(i)==int or type(i)==float:
        sum+=i
print(f"Total of elements is {sum}")
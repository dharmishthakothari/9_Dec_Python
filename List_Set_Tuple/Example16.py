lst={}
print(type(lst))
lst={1,2,3,4}
print(type(lst),lst)

lst.add(22)
print(lst)
lst.add(1)
print(lst)

# remove dublicate item from list witout using for loop

lst_numbers=[1,2,3,4,5,2,3,4]
lst_ans=set(lst_numbers)
print(lst_ans)
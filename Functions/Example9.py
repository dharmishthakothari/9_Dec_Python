lst_numbers=[1,2,3,4]
pow_numbers=[2,2,2,3]
# 1^2 , [1,4,9,256]
lst_ans=[]

# for i in range(len(lst_numbers)):
#     #lst_ans.append(lst_numbers[i]**pow_numbers[i])
#     lst_ans.append(pow(lst_numbers[i],pow_numbers[i]))

lst_ans=list(map(pow,lst_numbers,pow_numbers))
print(lst_ans)


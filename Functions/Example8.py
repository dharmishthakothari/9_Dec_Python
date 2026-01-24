lst_name=['sneha','ami','harmi']
upper_names=[]
# for i in lst_name:
#     upper_names.append(i.upper())

upper_names=list(map(str.upper,lst_name))

print(upper_names)

def sq(num):
    return num*num

lst_num=[1,2,3]
lst_ans=[]
# for i in lst_num:
#     lst_ans.append(sq(i))

lst_ans=list(map(sq,lst_num))
print(lst_ans)


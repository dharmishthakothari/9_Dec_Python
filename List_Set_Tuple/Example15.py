lst1=['Gujarat','Rajshan','Maharastra']
ans=[i for i in lst1 if len(i) > 7]
print(ans)
# print element whose len is more then 5
# append
# ans=[]
# for i in lst1:
#     if len(i)>7:
#         ans.append(i)
# print(ans)

lst2=[1,22,6]
ans=[i*i for i in lst2 if i %2==0]
print(ans)

#convert lst elemetn into upper case with list comprehensive 
ans=[i.upper() for i in lst1]
print(ans)

ans=(i.upper() for i in lst1)
print(list(ans))


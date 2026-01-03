lst1=['Gujarat','Rajshan','Maharastra']
lst2=['Gandhinagar','Jaipur','Mumbai']
ans=zip(lst1,lst2)
print(ans)
print(list(ans))

lst1=[1,2,3,4]
lst2=[1,2,9,16]
lst3=[1.8,27,64]
ans=list(zip(lst1,lst2,lst3))
print(ans)

data=[('Frans',"Paris"),('India','Delhi'),('Natherlands','Amsterdam')]
lst_country,lst_capital=zip(*data)
print(lst_country)
print(lst_capital)
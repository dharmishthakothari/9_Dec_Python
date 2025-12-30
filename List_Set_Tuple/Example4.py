#Convert to upper case if the len of list elemet is more then 5

lst_city=['ahmedabad','surat','rajkot',"sdftr"]
for i in lst_city:
    if len(i)>5:
        print(i.upper())

#Find length of each element from list
lst_city=['ahmedabad','surat','rajkot',"sdftr"]
for i in lst_city:
    print(f"{i} ---> {len(i)}")

for i in lst_city:
    for j in i:
        if j in "aeiouAEIOU":
            print(f"Vowel in {i}")
            break
# Count no of strings which starts with letter 'M' from list 
count=0
lst_name=['Mohit','Naresh','Harsh','Meet']
for i in lst_name:
    if i.startswith('M'):
        print(i)
        count+=1
print(f"No of strings startwith M are {count}")
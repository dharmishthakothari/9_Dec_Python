# calculate sum of all the marks 
# 120+150+200+110 = 
student_data ={
    "ami@gmail.com":["Ami",20,2345678,120],
    "riya@gmail.com":["Riya",21,455756,150],
    "Manish@yahoo.com":["manish",22,454354,200],
    "amitlah@gmail.com":['Amitlah',22,345345,110]
   }
sum=0 
for i,j in student_data.items():
    print(student_data[i][3])
    sum+=student_data[i][3]
print("Sum of all the marks ",sum)

# For Searching 

search=input("Please enter email ")
for i,j in student_data.items():
    if search==i:
        for i1 in j:
            print(i1)
        break
else:
    print(f"{search} not found in student data")


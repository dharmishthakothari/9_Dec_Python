student_data ={
    "ami@gmail.com":["Ami","20",2345678,120],
    "riya@gmail.com":["Riya",21,455756,150],
    "Manish@yahoo.com":["manish",22,454354,200],
    "amitlah@gmail.com":['Amitlah',22,345345,110]
   }
for i,j in student_data.items():
    print(i)
    for i1 in j:
        print("\t",i1)
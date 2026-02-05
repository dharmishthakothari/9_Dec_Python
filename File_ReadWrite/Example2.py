path="C:\\Users\\Admin\\Documents\\9_Dec_Python\\Conditional_stmt\\example2.py"
#file=open("C:\\Users\\Admin\\Documents\\Notes.txt")
file=open(path)
file.seek(25)
print(f"Start position {file.tell()}")
# while True:
#     data=file.readline()
#     print(data)
#     if not data:
#         break    

data=file.readlines()
for i in data:
    print(i)

print(f"End position {file.tell()}")
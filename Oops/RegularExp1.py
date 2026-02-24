import re
msg="Mega Ahemdabad city is Ahemdabad"

s=re.search(r"Ahemdabad",msg)
print(s)
if s:
    print("String is found")
else:
    print("String not found")

s1=re.findall(r"Ahemdabad",msg)
print(s1)
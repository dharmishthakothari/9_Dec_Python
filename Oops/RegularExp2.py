import re
msg= "This is 123 9090909090 is my contact and 8989898989 is your contact number"
s=re.search(r"\d{10}",msg)

print(s)
s1=re.findall(r"\d{10}",msg)
print(s1)
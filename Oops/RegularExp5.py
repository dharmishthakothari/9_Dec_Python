import re
str1="1tops@tops.com"
ans=re.findall(r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$",str1)
print(ans)
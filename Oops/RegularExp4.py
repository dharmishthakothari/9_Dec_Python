import re
str1="user4 test user1 user2 user dharmishtha user3"
ans=re.findall(r"\duser\d",str1)
print(ans)

str2="This ia Tops"
ans=re.search(r"[a-j]",str2)
print(ans.group())


# ans=re.findall(r"[a-j]",str2)
# print(ans)

ans=re.search(r"user\d","user user2")
print("result od search ",ans)
ans=re.match(r"user\d","user user2")

print("result of match ",ans)

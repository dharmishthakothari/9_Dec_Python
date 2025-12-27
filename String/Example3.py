name=input("Enter name ")
# for i in name:
#     print(i)

count=0
for i in name:
    if i in "aeiouAEIOU":
        count+=1
print(f"No of vowel in strng is {count}")

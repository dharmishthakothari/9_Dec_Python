dict1={1:"one",2:"two",3:"three",2:"Five",4:"Five"}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

print("Iterating keys")
for i in dict1.keys():
    print(i)

print("Iterating values")
for i in dict1.values():
    print(i)

print("Iterating keys-values")
for i,j in dict1.items():
    print(i,j)

print("Fetching values thru Iterating keys")
for i in dict1.keys():
    print(dict1[i])
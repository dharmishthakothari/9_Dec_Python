name=input("Enter name ")
# letter from 0 to 5
print(name[0:5])

# letters upto 7
print(name[:7])

# letters from 7 to end
print(name[7:])
print(name)

print(name[::1])

print(f"Use -ne indexing {name[-8:-2:2]}")

print(name[::-1])
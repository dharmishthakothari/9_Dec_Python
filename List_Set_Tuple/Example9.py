lst_numbers=[1,3,6,7,8,3,4,6,4,5,4]
lst_city=['ahmedabad','baroda','surat']

#lst_numbers.clear()
#del lst_numbers
del lst_numbers[2]
print(lst_numbers)

print(f"Pop() {lst_numbers.pop()}")
print(lst_numbers)

print(f"Pop(3) {lst_numbers.pop(3)}")
print(lst_numbers)

print(f"remove(4) {lst_numbers.remove(4)}")
print(lst_numbers)
lst_numbers.reverse()
print(f"After reverse {lst_numbers}")



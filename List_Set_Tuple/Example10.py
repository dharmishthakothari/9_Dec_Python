lst_numbers=[1,3,6,7,8,3,4,6,4,5,4]
lst_city=['ahmedabad','amereli','jamnagar','baroda','surat']
print(f"Original List {lst_numbers} - {lst_city}")
lst_numbers.sort(reverse=True)
lst_city.sort(reverse=True)
print(f"After Sort {lst_numbers} - {lst_city}")
lst_city=['ahmedabad','amereli','disha','jamnagar','baroda','surat']
# sort cities according to length 
lst_city.sort(key=len)
print(f"After sorting according to length {lst_city}")
print(sum(lst_numbers))

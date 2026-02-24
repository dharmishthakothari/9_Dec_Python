def gen():
    for i in range(1,6):
        #print("in")
        yield i

a=gen()
# for i in a:

#     print(i)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

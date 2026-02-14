class A:
    def __init__(self,name,c_no):
        self.__c_no=c_no
        self.name=name
    def display(self):
        print(self.__c_no,self.name)

a=A("test",1234567)
a.display()
print(a.name)
print(a.__c_no)
    
        
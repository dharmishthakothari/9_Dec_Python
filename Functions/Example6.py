def studentInfo(*args):
    print(args)

def employeeInfo(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

studentInfo('Ami',20)
studentInfo('sneha',23456)
studentInfo('Paldi')
studentInfo('Maitri',20,345345,'Paldi',250)
employeeInfo(name='Dharmishtha',address='Paldi')
employeeInfo(name='test',salary=20000)
employeeInfo(dept="Software",master="Python")

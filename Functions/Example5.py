def greet(msg="Have nice Day"):
    print(msg)

def studentInfo(name,address='Paldi',age=20):
    print(name,address,age)

def empInfo(name,c_no,salary=0.0,address="Paldi"):
    print(name,address,c_no,salary)

greet("Good Morning")
greet("Good Afternoon")
greet()
studentInfo('sneha','cg road')
studentInfo('ami','Paldi',19)
studentInfo('Riya')
studentInfo('eeee',age=21)
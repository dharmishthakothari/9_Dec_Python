class Mother:
    def greet1(self):
        print("From mother")
class Father:
    def greet2(self):
        print("From Father")
class Child(Mother,Father):
    pass

ch=Child()
ch.greet1()
ch.greet2()

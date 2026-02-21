class Car:
    def speed(self):
        pass
class Sports(Car):
    def speed(self):
        print("Fast")
class Sedan(Car):
    def speed(self):
        print("Normal")

obj=Car()
obj.speed()

obj1=Sports()
obj1.speed()

obj2=Sedan()
obj2.speed()
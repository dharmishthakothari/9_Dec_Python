from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def calculateInterest(self):
        pass
    def greet(self):
        print("Welcome")        
class SBI(Bank):

    def calculateInterest(self):
        return 0.5
class Axis(Bank):
    def calculateInterest(self):
        return 0.7
    
obj=SBI()
print(obj.calculateInterest())

# obj1=Bank()
# print(obj1.calculateInterest())
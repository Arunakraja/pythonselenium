# inheritance means acquiring properties of parent class
from Oops_2 import Calci

class Child(Calci):
    num2 = 200

    def __init__(self):
        print('This is a constructor method from child class getting executed automatically')
        Calci.__init__(self,2,10) # parent contructor

    def getCompleteData(self):
        return self.summation()+Child.num2+ Calci.num
         #112 +200+100
obj1Child = Child()
print(obj1Child.getCompleteData())



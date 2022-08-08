class Calci:
    num = 100 # class variable or Global variable

    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber= b
        print('firstnumber is', self.firstnumber)
        print('secondnumber is', self.secondnumber)
        print('This is a super method from parent class is executed when object child class object is created')

    def getData(self):
        print('I am a method getting executed insided a class')

    def summation(self):
        return self.firstnumber + self.secondnumber+ Calci.num

# obj1= Calci(2,3) # I am creating a object of the class calci.
# obj1.getData()
# print(obj1.summation())
#
# obj2 = Calci(4,2)
# obj2.getData()
# print(obj2.summation())
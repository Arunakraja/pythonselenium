 # OOps Priniciple
 # Classes are user defined, blue print or prototype
 # Class will have method, class variables, intance variable, constructor objects.

class Calculator:
    num = 100

    def getData(self):
        print('I am now executing as function in a class')



obj = Calculator() # we are creating the objects
print(obj.num)
obj.getData()

# Calculator class is acting as Idly mould
# Calculator() it acting as object or actual idlies
# obj -> Object reference variable like TV remote
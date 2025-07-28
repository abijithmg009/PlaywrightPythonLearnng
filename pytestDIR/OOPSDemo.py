#classes are user defined blueprint or prototype

#sum,multiplication,addition and constant

#class will have methods,variables, instances of variables,

class Calculator:
    num = 100 #class variable
    #default constructor
    def __init__(self,a,b):
        self.a = a
        self.b = b

        print("I'm called automatically while calling class")

    def getData(self):
        print("Executing the method inside class")


    def Summation(self):
        return self.a + self.b + Calculator.num



obj = Calculator(2,3)
obj.getData()
print(obj.Summation())

obj = Calculator(4,5)
obj.getData()
print(obj.Summation())

# self keyword is manditotry for calling variable names into method
# instance and class variable have while different purpose
#constructor name should in __init__
# new kayword is not required when you create object

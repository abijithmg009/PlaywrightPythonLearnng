#inheritance aquiring properties of parent class
# new child class can bring all objects and methods
from OOPSDemo import Calculator


class childimpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,5,6)

    def getComplete(self):
        return self.num2+ self.num + self.Summation()





obj3 = childimpl()
print(obj3.getComplete())
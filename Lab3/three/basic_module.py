import math

class basic_calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        return self.num1 + self.num2
    
    def subtraction(self):
        return self.num1 - self.num2
    
    def multiplication(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 == 0:
            return "Enter number other than ZERO"
        return self.num1 / self.num2
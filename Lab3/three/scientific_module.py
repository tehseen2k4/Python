from basic_module import basic_calc
import math

class s_calc(basic_calc):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    
    def factorial(self, n):
        if n < 0:
            return "Enter non-negative integer"
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)
    
    def x_power_y(self):
        return pow(self.num1, self.num2)
    
    def log(self):
        if self.num1 <= 0:
            return "Enter positive number"
        return math.log10(self.num1)
    
    def ln(self):
        if self.num1 <= 0:
            return "Enter positive number"
        return math.log(self.num1)
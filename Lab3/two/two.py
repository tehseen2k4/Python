from basic import basic_calc
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

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
            
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            basic = basic_calc(num1, num2)
            
            while True:
                print("\n=== Basic Calculator Menu ===")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Back to Main Menu")
                
                op_choice = input("Enter operation choice (1-5): ")
                
                if op_choice == '5':
                    break
                elif op_choice == '1':
                    print(f"Result: {basic.addition()}")
                elif op_choice == '2':
                    print(f"Result: {basic.subtraction()}")
                elif op_choice == '3':
                    print(f"Result: {basic.multiplication()}")
                elif op_choice == '4':
                    print(f"Result: {basic.division()}")
                else:
                    print("Invalid choice! Please try again.")
                    
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            scientific = s_calc(num1, num2)
            
            while True:
                print("\n=== Scientific Calculator Menu ===")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Power")
                print("6. Factorial (of first number)")
                print("7. Log (of first number)")
                print("8. Natural Log (of first number)")
                print("9. Back to Main Menu")
                
                op_choice = input("Enter operation choice (1-9): ")
                
                if op_choice == '9':
                    break
                elif op_choice == '1':
                    print(f"Result: {scientific.addition()}")
                elif op_choice == '2':
                    print(f"Result: {scientific.subtraction()}")
                elif op_choice == '3':
                    print(f"Result: {scientific.multiplication()}")
                elif op_choice == '4':
                    print(f"Result: {scientific.division()}")
                elif op_choice == '5':
                    print(f"Result: {scientific.x_power_y()}")
                elif op_choice == '6':
                    print(f"Result: {scientific.factorial(int(num1))}")
                elif op_choice == '7':
                    print(f"Result: {scientific.log()}")
                elif op_choice == '8':
                    print(f"Result: {scientific.ln()}")
                else:
                    print("Invalid choice! Please try again.")
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
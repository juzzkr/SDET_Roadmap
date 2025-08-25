class calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a*b
    def divide (self, a, b):
        if b == 0:
            return "Invalid as denominator can't be 0"
        return a / b
    
cal = calculator()
num1 = 10
num2 = 5

print(f"{num1} + {num2} = {cal.add(num1,num2)}")
print(f"{num1} - {num2} = {cal.subtract(num1,num2)}")
print(f"{num1} * {num2} = {cal.multiply(num1,num2)}")
print(f"{num1} / {num2} = {cal.divide(num1,num2)}")
        
class Calculator:
    def sum(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: division by zero"
        return a / b

    def multiply(self, num1, num2):
        return num1 * num2

    def sub(self, a, b):
        return a - b
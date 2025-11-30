class Calculator:
    
    def calculate(self,a,b,operation):
        operation = operation.lower()

        if operation == "add":
            return a+b
        elif operation == "subtract":
            return a-b
        elif operation == "multiply":
            return a*b
        elif operation == "divide":
            if b == 0:
                return "Error"
            else:
                return a/b
        else:
            return "Invalid operation"
        



# ---program---

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
operation = input("Enter operation(add/subtract/multiply/divide):")

calc = Calculator()
result = calc.calculate(a,b,operation)

print("Result:",result)
            
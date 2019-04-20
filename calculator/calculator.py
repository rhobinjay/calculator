class Calculator:

    def __init__(
        self,
        operation,
        number1,
        number2
    ):
        self.operation = operation
        self.number1 = number1
        self.number2 = number2
        self.result = None

    def calculate(self):
        execute = self.get_operation()
        self.result = execute()

    def get_operation(self):
        operation = {
            'add' : self.add,
            'subtract' : self.subtract
        }
        return operation[self.operation]

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

import unittest
from lib import Calculator

class Test_Calculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator(operation = "add", number1 = 4, number2 = 7)
        self.assertEqual(calculator.add(), 11)

    def test_subtract(self):
        calculator = Calculator(operation = "subtract", number1 = 10, number2 = 7)
        self.assertEqual(calculator.subtract(), 3)
    
    def test_calculate(self):
        calculator = Calculator(operation = "add", number1 = 10, number2 = 7)
        calculator.calculate()
        self.assertEqual(calculator.result, 17)
        calculator = Calculator(operation = "subtract", number1 = 8, number2 = 7)
        calculator.calculate()
        self.assertEqual(calculator.result, 1)

    def test_get_operation(self):
        calculator = Calculator(operation = "add", number1 = 10, number2 = 7)
        self.assertEqual(calculator.get_operation(), calculator.add)
        calculator = Calculator(operation = "subtract", number1 = 10, number2 = 7)
        self.assertEqual(calculator.get_operation(), calculator.subtract)

if __name__ == '__main__':
    unittest.main()
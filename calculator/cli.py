import sys
from calculator import argparser
from calculator.calculator import Calculator


def main():
    try:
        args = argparser.parse()

        calculator = Calculator(operation=args.operation, number1=args.number1, number2=args.number2)
        calculator.calculate()

        print("Result: ", calculator.result)

    except Exception as e:
        print(e)
    else:
        print('Success!')
    finally:
        print('Cleaning up.')


if __name__ == '__main__':
    sys.exit(main())

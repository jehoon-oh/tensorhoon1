from calculator.model import Calculator

if __name__ == '__main__':
    calc = Calculator(int(input('첫번째 수는? ')), int(input('두번째 수는? ')))
    print("{} + {} = {}".format(calc.first, calc.second, calc.sum()))
    print("{} - {} = {}".format(calc.first, calc.second, calc.sub()))
    print("{} * {} = {}".format(calc.first, calc.second, calc.mul()))
    print("{} / {} = {}".format(calc.first, calc.second, calc.div()))
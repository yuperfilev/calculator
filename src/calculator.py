from src.stack import *
from src.reverse_polish_notation import *
from src.exceptions import *

class Calculator:

    def __init__(self) -> None:
        self.rpn = RPN()
        self.s = Stack()
    
    def calculate(self, expression: str) -> float:
        notation = self.rpn.reverse_notation(expression)
        for elem in notation:
            if self.rpn.is_number(elem):
                self.s.push(float(elem))
            elif elem == '±':
                self.s.push(0 - float(self.s.pop()))
            elif elem == '√':
                try:
                    self.s.push(float(self.s.pop()**0.5))
                except TypeError:
                    raise IncorrectExpression("Отрицательное значение под корнем")
            else:
                value1 = self.s.pop()
                value2 = self.s.pop()
                if value1 == None or value2 == None:
                    raise IncorrectExpression("Введено некорректное выражение")
                elif elem == '^':
                    self.s.push(value2 ** value1)
                elif elem == '/':
                    if value1 != 0:
                        self.s.push(value2 / value1)
                    else:
                        raise ZeroDivisionError("Деление на ноль")
                elif elem == '*':
                    self.s.push(value2 * value1)
                elif elem == '-':
                    self.s.push(value2 - value1)
                elif elem == '+':
                    self.s.push(value2 + value1)
        return self.s.pop()
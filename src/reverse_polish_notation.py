from src.stack import Stack
from src.exceptions import *

PI = "3.14159265358979323846"
E = "2.71828182845904523536"

class RPN:

    def __init__(self) -> None:
        self.operations_priority = {
            '+': 0,
            '-': 0,
            '*': 1,
            '/': 1,
            '^': 2,
            '√': 2,
            '±': 3
        }

    def is_number(self, num: str) -> bool:
        try:
            if num[:2] == '00':
                return False
            float(num)
            return True
        except ValueError:
            return False
    
    def is_operation(self, operation: str) -> bool:
        if operation in self.operations_priority.keys():
            return True
        return False

    def reverse_notation(self, expression: str) -> list:
        expression = expression.replace(" ", "")
        reverse_polish_expression = []
        s = Stack()
        i = 0
        while i < len(expression):
            
            if '0' <= expression[i] <= '9':
                tmp = expression[i]
                while i+1 < len(expression) and ('0' <= expression[i+1] <= '9' or expression[i+1] == '.'):
                    tmp += expression[i+1]
                    i += 1
                if self.is_number(tmp):
                    reverse_polish_expression.append(tmp)
                else:
                    raise ValueError("Некорректные значения")

            elif expression[i] == '(':
                s.push(expression[i])

            elif expression[i] == ')':
                while True:
                    tmp = s.pop()
                    if tmp == '(':
                        break
                    elif tmp == None:
                        raise InconsistentBrackets("Несогласованные скобки в выражении")
                    else:
                        reverse_polish_expression.append(tmp)

            elif expression[i] == '-' and (i-1 < 0 or self.is_operation(expression[i-1])):
                s.push('±')

            elif expression[i] == 'п':
                reverse_polish_expression.append(PI)

            elif expression[i] == 'e':
                reverse_polish_expression.append(E)
           
            elif self.is_operation(expression[i]):
                while s.head() != None:
                    if s.head() != '(' and self.operations_priority[s.head()] >= self.operations_priority[expression[i]]:
                        reverse_polish_expression.append(s.pop())
                    else:
                        break
                s.push(expression[i])
            else:
                raise ValueError("Некорректные значения")
            i += 1
        while s.head() != None:
            tmp = s.pop()
            if self.is_operation(tmp):
                reverse_polish_expression.append(tmp)
            else:
                raise InconsistentBrackets("Несогласованные скобки в выражении")
        return reverse_polish_expression

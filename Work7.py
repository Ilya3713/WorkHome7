import operator
message = 'Ошибка!!!!  Введите формат например "+ 2 2"'
def calc(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op1 = expr.split(" ")[1]
            stack.append(float(op1))
            op2 = expr.split(" ")[2]
            stack.append(float(op2))
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
            return stack.pop()
            break
        else:
          return message
          
          
    
  
print(int(calc("+ 2 2 ")))
print(int(calc("- 2 2 ")))
print(int(calc("* 2 2 ")))
print(int(calc("/ 2 2 ")))
print(calc(" 2 2 /"))




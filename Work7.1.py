

def calc(number1, number2, oper):
  
  if oper == '+':
    print(number1 + number2)

  elif oper == '-':
    try:
      if isinstance(number1, str) or isinstance(number2, str):
        raise Exception('Вычитание строк запрещено')
      else:
        print(number1 - number2)
    except Exception as e:
      print(e)

  elif oper == '*':
    try:
      if isinstance(number1, str) or isinstance(number2, str):
        raise Exception('Умножение строк запрещено')
      else:
        print(number1 * number2)
    except Exception as e:
      print(e)
    
  elif oper == '/':
    try:
      if isinstance(number1, str) or isinstance(number2, str):
        raise Exception('Деление строк запрещено')
      else:
        print(number1 / number2)
    except ZeroDivisionError:
      print('Деление на 0 запрещено')
    except Exception as e:
      print(e)
  else:
    print('Ошибка!!!Введены некоректно данные')
    
    
try:
  Number_variant = input('a  - числа \n b - строки \n Выберите вариант работы: ')
  if Number_variant == 'a':
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    oper = input('Выберите операцию: ')
    assert oper in ['+','-','*','/']
    calc(number1, number2, oper) 
  elif Number_variant == 'b':
    number1 = input('Введите первую строку: ')
    number2 = input('Введите вторую строку: ')
    oper = input('Выберите операцию: ')
    calc(number1, number2, oper) 
  else:
   print('Выберите одно из двух вариантов')

  
except TypeError:
 print('Ошибка!!!Не верное количество аргументов')
except AssertionError:
 print('Ошибка!!!Не доступен данный оператор')
except ValueError:
  print('Ошибка!!!Не удалось str преобразовать в int')

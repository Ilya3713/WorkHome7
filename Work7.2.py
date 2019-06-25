 ##Функция с исключением KeyError вызывается "list_pKeyError"
 ## Переписал функцию people т.к в ней получали имя человека по номеру. Так же добавил исключения
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006"}
      ],

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def list_pKeyError():
  for item in documents:
      for s in item:
        try:
          if s.keys() == s.keys():
            print(f'{s["type"]} "{s["number"]}" "{s["name"]}"')
        except KeyError:
          print('Нет  ключа ["name"] по документу: ', s['number'] )



def people(number_doc):
  for item in documents:
    for s in item:
      if number_doc == s['number']:
        try:
          names = s['name']
          print(f'Владелец документа {names}')
          break
        except KeyError:
          print('Нет ключа name')   
          break
    else:
      print("Нет указанного документа")
      break


# def list_p():
#   for item in documents:
#     for s in item:
#       if s.keys() == s.keys():
#         print(f'{s["type"]} "{s["number"]}" "{s["name"]}"')


def shelf(number_doc):
  for d in directories:
    if str(number_doc) in directories.get(d):
      print(" № Полки где лежит ваш документ:", d)
      break
  else:
    print('Вашего документа нет')


def add(name, type_doc, number_doc, number_p):
  for item in documents:
    item.append({"type": type_doc, "number": number_doc, "name": name},)
    
  for item in directories:
    if item == str(number_p):
      subway = item
      directories.setdefault(subway, list())
      directories[subway].append(number_doc)
      break
  else:
    directories.setdefault(str(number_p), list())
    directories[str(number_p)].append(number_doc)
      
  print(f'Обновленый словарь с полками: {directories}  \n')
  print(f'Обновленый список с документами: {documents}  \n')
    

def move(number_doc, number_p):
  for item in directories:
    if number_doc  in directories.get(item):
      directories[item].remove(number_doc)
      for items in directories:
        if number_p == items :
          subway = items
          directories.setdefault(subway, list())
          directories[subway].append(number_doc) 
          print(f'Вы перенесли свой документ на полку №:{items}')
          print(directories)
          return
      else:
        print('Нет такой полки')
        break
  else:
    print('Нет данного номера документа ')
    
    
def inputData(doc):
  if doc == 'p':
    number_doc = input('Введите номер документа: ')
    people(number_doc)
  # elif doc == 'l':
  #   list_p()
  elif doc == 'lk':
    list_pKeyError()
  elif doc == 's':
    number_doc = input('Введите номер документа: ')
    shelf(number_doc)
  elif doc == 'a':
    name = input('Введите вашу Фамилию и Имя: ')
    type_doc = input('Введите тип документа: ')
    number_doc = input('Введите номер документа: ')
    number_p = int(input('Введите на какой  полке будет лежать ваш документ: '))
    add(name, type_doc, number_doc, number_p)
  elif doc == 'm':
    number_doc = input('Введите номер документа: ')
    number_p = input('Введите номер полки: ')
    move(number_doc, number_p)


   
##Функция с исключением KeyError вызывается "lk"
## Переписал функцию people т.к в ней получали имя человека по номеру. Так же добавил исключения
name_com = input("Введите пользовательскую команду(p, s, a, m, lk): ")
inputData(name_com)


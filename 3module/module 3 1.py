calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
   count_calls()
   return (len(string),
           string.upper(),  # Возвращает кортеж из длины строки, строки в верхнем и нижнем регистре
           string.lower()
           )

def is_contains(string, list_to_search):
    count_calls()
    for list in list_to_search:  # перебираем список
        if string.casefold() == list.casefold():  # Сравнение строк без учёта регистра
            return True  # если строка найдена то возвращаем True
    return False  # иначе False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)

my_dict = {'Filip': 2004, 'Igor' : 1996, 'Franchesk' : 2020} # словарь
print(my_dict)
print(my_dict['Filip']) # вывод одного из существующих занчение в словаре
print(my_dict .get('Vanya')) # вывод несуществующего значени в словаре
my_dict .update({'Petya': 1859, 'Victor': 1999}) #добавление в словарь
print(my_dict .pop('Igor')) #удаление из словаря
print(my_dict)
my_set = {253,True,'Filin',253, False, 158, False } # множество содержит уникальные типы данных
print(my_set)
my_set.update (('bigbon', 28)) # добавление элементов во множества
my_set .discard('Filin') # удаление элемента из множества
print(my_set)

from pprint import pprint


class Introspection:
    def __init__(self, car_name, car_age):
        self.car_name = car_name
        self.car_age = car_age

    def car_owner(self):
        return f"I own an {self.car_name} brand, it was built in {self.car_age}"


def introspection_info(obj):
    info = {'Тип': type(obj), 'Атрибуты': dir(obj)}
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['Методы'] = methods

    try:
        info['Модуль'] = obj.__module__

    except AttributeError:
        info['Модуль'] = 'Не определен'

    if isinstance(obj, list):
        info['Количество элементов'] = len(obj)

    elif isinstance(obj, dict):
        info['Количество пар ключ-значение'] = len(obj)

    elif isinstance(obj, str):
        info['Длина текста'] = len(obj)
        info['Первые 3 символа'] = obj[:3]

    elif hasattr(obj, "__doc__"):
        info['Документация'] = obj.__doc__

    return info


info_cars = Introspection('Audi', 2000)
my_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
my_dict = {'Toyota': 2000, 'Opel': 2010, 'Jeep': 1933}
my_string = 'A world-class driver'

print(info_cars.car_owner())
pprint(introspection_info(info_cars))
print(my_list)
pprint(introspection_info(my_list))
print(my_dict)
pprint(introspection_info(my_dict))
print(my_string)
pprint(introspection_info(my_string))

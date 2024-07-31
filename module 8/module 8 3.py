class IncorrectVinNumber(Exception):
    def __init__(self, message='Некоректный VIN номер'):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message='Некорректный номер автомобиля'):
        self.message = message


class Car:

    def __init__(self, model, vin_numbers, numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(vin_numbers)
        self.__numbers = self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_numbers):
        if isinstance(vin_numbers, str):
            raise IncorrectVinNumber('VIN номер должен быть числом')
        if vin_numbers < 1000000 or vin_numbers > 9999999:
            raise IncorrectVinNumber('VIN номер должен быть в диапазоне от 1000000 до 9999999')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Номер автомобиля должен быть строкой')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Номер автомобиля должен содержать 6 цифр')
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as e:
    print(e.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as e:
    print(e.message)
else:
    print(f'{second.model} успешно создан')

try:
    second = Car('Model2', 3000, 'т001тр')
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as e:
    print(e.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as e:
    print(e.message)
except IncorrectCarNumbers as ex:
    print(ex.message)
else:
    print(f'{third.model} успешно создан')

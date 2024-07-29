def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы: {num}')
            incorrect_data += 1

    return result, incorrect_data


def colculate_average(numbers):
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        if isinstance(numbers, (list, tuple, set)):
            return total_sum / (len(numbers) - incorrect_data)
        return 0

    except ZeroDivisionError:
        return 0
    except TypeError as exc:
        print(f'В numbers записан некорректный тип данных {exc}')
        return None


print(f'Результат 1: {colculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {colculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {colculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {colculate_average([42, 15, 36, 13])}')  # Всё должно работать

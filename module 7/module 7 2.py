def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            start_byte = file.tell()  # Получаем текущую позицию в файле
            file.write(string + '\n')
            strings_positions[(len(strings_positions) + 1, start_byte)] = string  # Добавляем позицию и строку в словарь
    return strings_positions

# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
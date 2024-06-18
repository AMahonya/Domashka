def  calculate_structure_sum(data_structure):
    summa = 0


    if isinstance(data_structure, dict):
        for key, value in data_structure.items():  #перебираем словарь
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:  #перебираем список, кортеж и множество
            summa += calculate_structure_sum(item)
    elif isinstance(data_structure, (int, float)):
        summa += data_structure  # прибовляем к общей сумме если элемент являеться целым числом или с плавающей точкой
    elif isinstance(data_structure, str):  # прибовляем к общей сумме в случие того если элемент являеться строкой
        summa += len(data_structure)

    return summa


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

result = calculate_structure_sum(data_structure)
print(result)
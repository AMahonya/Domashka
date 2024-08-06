first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(s) for s in first_strings if len(s) >= 5]
print(first_result)

second_result = [(f,s) for f in first_strings for s in second_strings if len(s) == len(f)]
print(second_result)

combined_list = first_strings + second_strings
third_result = {c: len(c) for c in combined_list if len(c) % 2 == 0}
print(third_result)
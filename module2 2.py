first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first==second==third:
    print("Равны все ", 3 , " числа")
elif first==second or second==third or third==first:
    print('Равны только ', 2, 'числа')
else:
    print("Равинств " ,0 )
    print("Попробуй еще раз ")
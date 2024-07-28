class Figure:
    sides_count = 0
    """
    Это базовый класс фигуры, который описывает общие свойства и методы для всех фигур
    """

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = list(sides)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 and isinstance(x, int) for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print("Недопустимый цвет. Значения красного, зеленого, синего цветов должны быть в диапазоне от 0 до 255.")

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(x, int) and x > 0 for x in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Недопустимое число сторон. число сторон должно быть равно количеству сторон фигуры.")


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, int(2 * 3.14 * radius))
        self.__radius = radius

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5 / a

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides_length):
        super().__init__(color, *[sides_length] * self.sides_count)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


# Создание объектов
circle = Circle((200, 200, 100), 10) # (Цвет, стороны)
triangle = Triangle((227, 38, 119), 10, 6, 8)
cube = Cube((222, 35, 130), 6)

print(circle.get_square())  # Площадь круга
print(triangle.get_square())  # Площадь треугольника
print(cube.get_volume())  # Объём куба
print(triangle.get_color())
print(triangle.get_sides())



# Проверка на изменение цветов:
circle.set_color(55, 66, 77)  # Изменится
print(circle.get_color())
cube.set_color(300, 70, 15)  # Не изменится
print(cube.get_color())


# Проверка на изменение сторон:
cube.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube.get_sides())
circle.set_sides(15)  # Изменится
print(circle.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle))
print(len(cube))
print(len(triangle))

# Проверка объёма (куба):
print(cube.get_volume())

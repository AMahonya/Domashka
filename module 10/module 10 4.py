import threading
from queue import Queue
import time
import random


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guet_arrival(self, *guests):
        for guest in guests:
            if any(table.guest is None for table in self.tables):
                for table in self.tables:
                    if table.guest is None:
                        table.guest = guest
                        guest.start()
                        print(f"{guest.name} сел (-а) за стол {table.number},")
                        break

            else:
                self.queue.put(guest)
                print(f"{guest.name} ожидает свободный стол.")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():  # Проверка, закончил ли гость прием пищи
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла).")
                    print(f"Стол № {table.number} свободен.")
                    table.guest = None  # Освобождение стола

                    # Проверка, есть ли гости в очереди
                    if not self.queue.empty():
                        new_guest = self.queue.get()  # Выход из очереди
                        table.guest = new_guest  # Посадка гостей за стол
                        print(f"{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол № {table.number}.")
                        new_guest.start()  # Запуск потока
            time.sleep(1)  # Пауза для имитации обслуживания


if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guet_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()

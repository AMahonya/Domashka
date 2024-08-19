from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.max_power = 100

    def run(self):
        print(f"{self.name} На нас напали стражи")
        day_counter = 0
        while self.max_power > 0:
            self.max_power -= self.power
            day_counter += 1

            print(f"{self.name} сражается {day_counter}-е сутки, осталось {self.max_power} стражей ")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя: {day_counter}-е сутки")


if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы окончены! ")

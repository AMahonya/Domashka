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
            if self.max_power >= self.power:
                self.max_power -= self.power
            else:
                self.power = self.max_power
                self.max_power = 0

            day_counter += 1
            print(f"{self.name} сражается {day_counter}-е сутки, осталось {self.max_power} стражей ")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя: {day_counter}-е сутки")


if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 48)
    second_knight = Knight("Sir Galahad", 9)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы окончены! ")

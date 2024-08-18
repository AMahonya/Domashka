from time import sleep
from datetime import datetime
from threading import Thread
from colorama import Fore, Style


def write_words(word_count, file_name):
    start_time = datetime.now()
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write('Какое-то слово № ' + str(i) + '\n')
            sleep(0.1)
        print(f"Завершилась записано в файл: {Fore.GREEN} {file_name}{Style.RESET_ALL}")
    time_end = datetime.now()
    print(f"Время выполнения записи в функции:{Fore.RED} {time_end - start_time} {Style.RESET_ALL}")


start_time = datetime.now()
write_words(10, "exemple1.txt")
write_words(30, "exemple2.txt")
write_words(200, "exemple3.txt")
write_words(100, "exemple4.txt")
time_end = datetime.now()

print(f"{Fore.RED}<== Работа без потоков завершена в {time_end - start_time} ==>{Style.RESET_ALL}")

f1 = Thread(target=write_words, args=(10, "exemple5.txt"))
f2 = Thread(target=write_words, args=(30, "exemple6.txt"))
f3 = Thread(target=write_words, args=(200, "exemple7.txt"))
f4 = Thread(target=write_words, args=(100, "exemple8.txt"))

start_time = datetime.now()

f1.start()
f2.start()
f3.start()
f4.start()

f1.join()
f2.join()
f3.join()
f4.join()

time_end = datetime.now()

print(f"{Fore.RED}<==Работа потока завершена в {time_end - start_time}==>{Style.RESET_ALL}")

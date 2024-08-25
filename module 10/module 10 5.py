# import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


if __name__ == '__main__':
    file_names = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.datetime.now()
    for file_name in file_names:
        read_info(file_name)
    end_time = datetime.datetime.now()
    print(f'Время выполнения чтения без использования multiprocessing: {end_time - start_time} сек.')

    # start_time = datetime.datetime.now()
    # with multiprocessing.Pool(processes=2) as pool:
    #     pool.map(read_info, file_names)
    # end_time = datetime.datetime.now()
    # print(f'Время выполнения чтения с использованием multiprocessing: {end_time - start_time} сек.')

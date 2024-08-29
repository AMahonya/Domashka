import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

with sqlite3.connect('inventory.db') as db:

    # создаём таблицы

    db.execute('''
        CREATE TABLE IF NOT EXISTS Товары (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Наименование TEXT,
            Цена REAL,
            Количество INTEGER
        )
    ''')

    db.execute('''
        CREATE TABLE IF NOT EXISTS Оборот (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Товар_id INTEGER,
            Дата TEXT,
            Тип TEXT,
            Количество INTEGER,
            FOREIGN KEY(Товар_id) REFERENCES Товары(id)            
        )
    ''')

    # добавляем товары

    db.execute('''
        INSERT INTO Товары (Наименование, Цена, Количество) VALUES
        ('Телевизор', 24800, 5),
        ('Ноутбук', 68700, 10),
        ('Пылесос', 9600, 5),
        ('Чайник', 1850, 25),
        ('Приставка', 2580, 12)
    ''')

    db.execute('''
            INSERT INTO Оборот (Товар_id, Дата, Тип, Количество) VALUES
            (10856, '2023-10-27', 'приход', 2),
            (20568, '2024-08-25', 'расход', 8),
            (35687, '2020-12-08', 'приход', 3),
            (12987, '2024-04-17', 'приход', 20),
            (11397, '2022-01-28', 'расход', 10)
        ''')
    db.commit()

    # читаем данные  отдельно из каждой таблицы БД

    technic_df = pd.read_sql_query('SELECT * FROM Товары', db)
    turnover_df = pd.read_sql_query('SELECT * FROM Оборот', db)

    # Анализ данных

    print("\n<=Общая информация о товарах=>")
    print(technic_df.describe())
    print("\n<=Товар с наибольшим количеством на складе=>")
    print(technic_df[technic_df['Количество'] == technic_df['Количество'].max()])
    print("\n<=Общая стоимость товара на складе=>")
    sum_technic = (technic_df['Цена'] * technic_df['Количество']).sum()
    print(f"Общая стоимость: {sum_technic}")
    print("\n<=Анализ движения товаров=>")
    print(turnover_df.groupby("Тип")["Количество"].sum())

    # График распределения товаров на складе

    plt.figure(figsize=(8, 6))
    plt.hist(technic_df["Количество"], bins=10, edgecolor='black')
    plt.title("Распределение количества товаров на складе")
    plt.xlabel("Количество")
    plt.ylabel("Частота")
    plt.show()

    # График движения товара по времени

    turnover_df['Дата'] = pd.to_datetime(turnover_df['Дата'])
    turnover_df = turnover_df.groupby(['Дата', 'Тип'])['Количество'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(turnover_df[turnover_df['Тип'] == 'приход']['Дата'],
             turnover_df[turnover_df['Тип'] == 'приход']['Количество'], label='Приход')
    plt.plot(turnover_df[turnover_df['Тип'] == 'расход']['Дата'],
             turnover_df[turnover_df['Тип'] == 'расход']['Количество'], label='Расход')
    plt.xlabel("Дата")
    plt.ylabel("Количество")
    plt.title("Движение товара по времени")
    plt.legend()
    plt.show()

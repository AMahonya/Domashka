import sqlite3
import random



connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


#  Заполняем таблицу 10 пользователями

# for i in range(1,11):
#      cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
#                     (f"User{i}", f'example{i}@gmail.com',
#                      random.randint(2, 9)*10,
#                      random.choice([500, 1000])))

#  Обновляем баланс через каждую 2 запись. начиная с 1 го пользователя

# cursor.execute("SELECT id, balance FROM Users")
# users = cursor.fetchall()
#
# for index, user in enumerate(users, start=1):
#     if index % 2 == 1:
#         cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, user[0],))

#  Удаляем каждого 3 его пользователя

# cursor.execute("SELECT id FROM Users")
# users = cursor.fetchall()
# for index, user in enumerate(users, start=1):
#     if index % 3 == 1:
#         cursor.execute("DELETE FROM Users WHERE id = ?", (user[0],))

# Выбор пользователей у которых возраст не равен 60 с выводом в консоль

# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
# users = cursor.fetchall()
#
# for user in users:
#     username, email, age, balance = user
#     print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")


# Удаляем пользователя с id = 6

# cursor.execute("DELETE FROM Users WHERE id = ?", (6,))


# Считаем общее количество записей в таблице

cursor.execute("SELECT COUNT(*) FROM Users")
count = cursor.fetchone()[0]
print(f'Общее количество записей в таблице: {count}')

# Считаем сумму баланса всех пользователей

cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchone()[0]
print(f'Сумма баланса всех пользователей: {sum_balance}')

# Высчитываем средний баланс всех пользователей

cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(f'Средний баланс всех пользователей: {avg_balance}')




connection.commit()
connection.close()
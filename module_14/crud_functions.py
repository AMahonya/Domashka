import sqlite3

DATABASE = 'products.db'

def initiate_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
            )
        ''')

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, description, price FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

def add_products():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    products = [
        ('Amino Isolate', '280 гр ', 1990),
        ('Amino Tabs ', '200 таблеток ', 3200),
        ('Mega Mass', '3000 гр', 8229),
        ('Whey Protein ', '1000 гр ', 6555)
    ]
    cursor.executemany('INSERT INTO products (title, description, price) VALUES (?, ?, ?)',
                       products)
    conn.commit()
    conn.close()

def add_user(username, email, age):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
                   (username, email, age, 1000))
    conn.commit()
    conn.close()

def is_included(username):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Users WHERE username =?', (username,))
    count = cursor.fetchone()
    conn.close()
    return count[0] > 0
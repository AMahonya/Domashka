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








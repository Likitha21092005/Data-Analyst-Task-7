import sqlite3

# Create and connect to the database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    sale_date TEXT NOT NULL
)
''')

# Insert sample data
sample_sales = [
    ('Laptop', 5, 999.99, '2023-01-15'),
    ('Phone', 10, 699.99, '2023-01-15'),
    ('Tablet', 8, 349.99, '2023-01-16'),
    ('Laptop', 3, 999.99, '2023-01-17'),
    ('Phone', 7, 699.99, '2023-01-18'),
    ('Headphones', 15, 99.99, '2023-01-19'),
    ('Tablet', 4, 349.99, '2023-01-20'),
    ('Headphones', 10, 99.99, '2023-01-21')
]

cursor.executemany('INSERT INTO sales (product, quantity, price, sale_date) VALUES (?, ?, ?, ?)', sample_sales)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database 'sales_data.db' created with sample data.")
import sqlite3

# Connect (creates file automatically)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    studytime INTEGER,
    absences INTEGER,
    G1 INTEGER,
    G2 INTEGER,
    predicted_G3 REAL
)
''')

conn.commit()
conn.close()

print("Database created successfully!")
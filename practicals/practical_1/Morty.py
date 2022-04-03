import sqlite3

connection = sqlite3.connect("morty.db")

cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dogs(
        name TEXT,
        age INTEGER,
        color TEXT
        )""")


def insert_into_db(name: str, age: int, color: str):
    cursor.execute(f"INSERT INTO dogs VALUES('{name}', {age}, '{color}')")
    connection.commit()


insert_into_db("Hachiko", 12, "red")
insert_into_db("Bim", 3, "White")
insert_into_db("Kupata", 2, "White")

print(cursor.execute('SELECT * FROM dogs').fetchall())

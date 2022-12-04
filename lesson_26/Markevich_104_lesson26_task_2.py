import sqlite3
import random

conn = sqlite3.connect('test_2.db')
cursor = conn.cursor()


def new_table():
    """The function creates a table in the database."""

    cursor.execute('''CREATE TABLE IF NOT EXISTS tab_0(id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                       col_1 INTEGER, 
                                                       col_2 INTEGER)''')


def insert_data(number_of_lines):
    """The function inserts data into a database table."""

    command = """INSERT INTO tab_0(col_1, col_2) VALUES(?,?)"""

    for _ in range(number_of_lines):
        cursor.execute(command, (random.randint(1, 10), random.randint(1, 10)))

    conn.commit()


def main():
    new_table()
    insert_data(10)

    # Вычисляем среднее значение по двум стобцам в таблице tab_0
    average = sum(list(*cursor.execute('''SELECT AVG(col_1), AVG(col_2) FROM tab_0'''))) / 2
    # Вычисляем количество записей в таблице tab_0
    number_of_records = list(*cursor.execute('''SELECT COUNT(*) FROM tab_0'''))[0]

    if average > number_of_records:
        print("Delete the fourth line.")
        cursor.execute('''DELETE FROM tab_0 WHERE id = 4''')
        conn.commit()
    else:
        print("Everything is fine.")

    # Выводим результат в консоль
    cursor.execute('''SELECT * FROM tab_0''')
    print(cursor.fetchall())


main()

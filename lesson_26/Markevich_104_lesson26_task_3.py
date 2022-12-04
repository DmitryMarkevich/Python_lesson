import sqlite3
import random

conn = sqlite3.connect('test_3.db')
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
    insert_data(int(input("Введите число (количество строк для базы данных): ")))

    # Берем из базы данных рандомно одну запись
    random_entry = cursor.execute('''SELECT * FROM tab_0 ORDER BY RANDOM() LIMIT 1''')
    # Распаковываем одну запись из базы данных на переменные
    id_, col_1, col_2 = list(*random_entry)
    print(id_, col_1, col_2)
    if col_1 % 2 == 0 and col_2 % 2 == 0:
        print("Delete this entry.")
        cursor.execute(f'''DELETE FROM tab_0 WHERE id = {id_}''')
        conn.commit()
    else:
        print("We are updating this post.")
        cursor.execute(f'''UPDATE tab_0 SET col_1 = 2, col_2 = 2 WHERE id = {id_}''')
        conn.commit()

    print(*cursor.execute('''SELECT * FROM tab_0'''))


main()

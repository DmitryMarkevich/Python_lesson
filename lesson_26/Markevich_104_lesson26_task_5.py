import sqlite3
import random

conn = sqlite3.connect('test_5.db')
cursor = conn.cursor()


def new_table():
    """The function creates a table in the database."""

    cursor.execute('''CREATE TABLE IF NOT EXISTS tab_0(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                       male_names TEXT,
                                                       female_names TEXT)''')


def insert_data(number_of_lines):
    """The function inserts data into a database table."""

    command = """INSERT INTO tab_0(male_names, female_names) VALUES(?,?)"""

    list_1, list_2 = ['Oliver', 'Jack', 'Harry', 'Jacob', 'Thomas'], \
                     ['Anna', 'Maria', 'Sophia', 'Katherine', 'Victoria']

    for _ in range(number_of_lines):
        cursor.execute(command, (random.choice(list_1), random.choice(list_2)))

    conn.commit()


def write_to_file(file):
    """The function writes data to a text file."""

    with open(file, 'w', encoding='utf-8') as file:
        file.write(' '.join([str(i) for i in list(*cursor.execute('''SELECT * FROM tab_0 WHERE id = 3'''))]))


def main():
    new_table()
    insert_data(3)

    print(*cursor.execute('''SELECT * FROM tab_0'''))

    # Удаляем первые две записи в базе данных
    cursor.execute(f'''DELETE FROM tab_0 WHERE id IN (1, 2)''')
    conn.commit()
    print(*cursor.execute('''SELECT * FROM tab_0'''))

    # Обновляем третью запись в базе данных
    cursor.execute(f'''UPDATE tab_0 SET male_names = 'HELLO', female_names = 'WORLD' WHERE id = 3''')
    conn.commit()
    print(*cursor.execute('''SELECT * FROM tab_0'''))

    # Записываем данные в txt файл
    write_to_file('test_5.txt')


main()

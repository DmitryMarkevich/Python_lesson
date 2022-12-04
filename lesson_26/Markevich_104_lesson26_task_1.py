import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()


def insert_data(line, col_1, col_2):
    """The function inserts values into the database."""

    command = """INSERT INTO tab_0(col_1, col_2, col_3) VALUES(?,?,?)"""

    for _ in range(line):
        col_3 = int(input("Введите число: "))
        cursor.execute(command, (col_1, col_2, col_3))
    conn.commit()


def main():
    # Создаем таблицу
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS
            tab_0(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            col_1 TEXT,
            col_2 TEXT,
            col_3 INTEGER
        )
        ''')

    # Вставляем значения в базу данных
    insert_data(2, 'HELLO_2', 'apple_2')

    # Выводим в консоль содержимое базы данных
    for i in cursor.execute('''SELECT * FROM tab_0'''):
        print(*i)


main()

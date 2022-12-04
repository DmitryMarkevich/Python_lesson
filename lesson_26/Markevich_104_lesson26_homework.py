import sqlite3

conn = sqlite3.connect('homework.db')
cursor = conn.cursor()


def new_table():
    # Создаем таблицу с колонкой для текстовых значений
    cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
    # Создаем таблицу с колонкой для числовых значений
    cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')


def line_processing(element):
    command = '''INSERT INTO tab_1(col_1) VALUES(?)'''
    cursor.execute(command, (element,))
    command = '''INSERT INTO tab_2(col_1) VALUES(?)'''
    cursor.execute(command, (len(element),))


def number_processing(element):
    if element % 2 != 0:
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES('нечетное')''')
    else:
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES(?)''', (element,))


data_list = [5, 'HELLO', 4, 'select', 100, 'table', 7, 'integer', 48, 'autoincrement']


def main():
    new_table()

    for elem in data_list:
        if isinstance(elem, str):
            line_processing(elem)

        if isinstance(elem, int):
            number_processing(elem)

        conn.commit()

    if list(*cursor.execute('''SELECT COUNT(*) FROM tab_2'''))[0] > 5:
        cursor.execute('''DELETE FROM tab_2 WHERE id = 1''')
        conn.commit()
    else:
        cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id = 1''')
        conn.commit()


main()
print(*cursor.execute('''SELECT * FROM tab_1'''))
print(*cursor.execute('''SELECT * FROM tab_2'''))

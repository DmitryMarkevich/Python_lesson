import sqlite3


class DataBase(object):
    """The class creates an object to work with the database."""

    DATA = 'test_4.db'
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, data=DATA):
        self.conn = sqlite3.connect(data)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.__instance = None

    def create_table(self, command):
        """The method creates a table in the database."""
        self.cursor.execute(command)

    def insert_data(self, command):
        """The method inserts values into the database."""
        self.cursor.execute(command)
        self.conn.commit()

    def select_data(self, command):
        """The method returns data based on the 'command' request."""
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def delete_data(self, command):
        """Method deletes data based on 'command' request."""
        self.cursor.execute(command)
        self.conn.commit()


def main():
    db1 = DataBase()
    create_tab = '''CREATE TABLE IF NOT EXISTS tab_0(id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                    col_1 INTEGER, 
                                                    col_2 INTEGER)'''
    db1.create_table(create_tab)

    select_1 = '''SELECT * FROM tab_0'''
    del_all = '''DELETE FROM tab_0'''

    while True:
        print("""
        Работаем с базой данных. 
        Выберите действие: 
                            1 - просмотреть данные 
                            2 - вставить данные 
                            3 - выбрать данные 
                            4 - удалить данные
                            Нажмите 'Enter', что бы выйти. 
                            """)
        ch = input("Ваш выбор: ")

        if ch == '':
            print("До свидания.")
            break
        elif ch == '1':
            print(db1.select_data(select_1))
        elif ch == '2':
            vel_1, vel_2 = int(input("Введите первое число: ")), int(input("Введите второе число: "))
            db1.insert_data(f'''INSERT INTO tab_0(col_1, col_2) VALUES({vel_1},{vel_2})''')
            print("Данные сохранены.")
        elif ch == '3':
            id_1 = int(input("Введите 'id' записи которую нужно вывести в консоль: "))
            sel = db1.select_data(f'''SELECT * FROM tab_0 WHERE id >= {id_1}''')
            print(sel if sel else "Такие данные отсутствуют! Введите другой 'id'.")
        elif ch == '4':
            print("Введите '1' если хотите удалить одну запись. Нажмите 'Enter', что бы удалить все данные.")
            ch_1 = input("Ваш выбор:")
            if ch_1 == '1':
                id_2 = int(input("Введите 'id' записи которую нужно удалить: "))
                db1.delete_data(f'''DELETE FROM tab_0 WHERE id = {id_2}''')
                print("Данные удалены!")
            elif ch_1 == '':
                db1.delete_data(del_all)
            else:
                print("Вы перешли в главное меню.")
        else:
            print(f"В меню нет пункта {ch}.")


main()

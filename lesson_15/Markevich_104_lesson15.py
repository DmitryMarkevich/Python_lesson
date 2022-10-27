import json


def request() -> dict:
    """
    The function asks the user for information about the purchase in the following format:
    purchase name, space, purchase price.
    Returns a dictionary in which the name of the product is the key, the cost of the product is the value.

    """
    product_list = []
    answer = ''
    while answer != "stop":
        answer = input("Введите название и стоимость продукта через пробел или stop чтобы выйти: ")
        if answer != 'stop':
            list_with_one_item = answer.strip().split()
            if len(list_with_one_item) == 2 and list_with_one_item[-1].replace('.', '').isdigit():
                product_list.append(list_with_one_item)
            else:
                print("Нужно вводить название продукта, пробел и его стоимость.")

    my_data = dict(product_list)

    return my_data


def write_to_json_file(target_file: str) -> None:
    """
    The function takes a dictionary and writes it to a json file.

    """

    with open(target_file, 'w', encoding='utf-8') as file:
        json.dump(request(), file, ensure_ascii=False)


def read_json_file(target_file: str) -> dict:
    """
    The function reads a json file and returns a dictionary with data if the json file exists,
    if the file does not exist it returns an empty dictionary.

    """
    try:
        with open(target_file, encoding='utf-8') as file:
            data = json.load(file)

        return data

    except FileNotFoundError:

        return {}


def calculate_purchase(dict_: dict) -> float:
    """
    The function takes a dictionary.
    Returns the sum of all dictionary values.

    """
    return sum([float(i) for i in dict_.values()])


def main():
    """
    main function.

    """
    data_file_json = 'product_database.json'

    while True:
        print("""Программа для расчета стоимости покупки.
        
                0 - выйти из программы
                1 - сделать покупку
                2 - рассчитать стоимость
                """)

        choice = input("Ваш выбор: ")

        if choice == '0':
            break
        elif choice == '1':
            write_to_json_file(data_file_json)
        elif choice == '2':
            print(f"Итого по чеку: {calculate_purchase(read_json_file(data_file_json))} руб.\n")
        else:
            print("Такого пункта нет в меню.")

    print('\t' * 4 + "До свидания.")


main()

def sort_by_key_length(base_dict: dict) -> dict:
    """
    The function takes a dictionary.
    Returns a dictionary sorted by key length.

    """
    return dict(sorted(base_dict.items(), key=lambda x: len(x[0])))


# Исходные словари:
dict_1 = {'верный': [11, 55.2, 'слон'], 'фиолетовый': 15, 'орда': 'восемь'}
dict_2 = {'ода': {52, 99, 2}, 'сороконожка': {110, 'слово', 15}}

# Объединяем два словаря в один
dict_3 = {**dict_1, **dict_2}
print("Исходный словарь:")
print(dict_3)

print("Отсортированный по длине ключей:")
print(sort_by_key_length(dict_3))

import itertools


def slice_objects(O, idexes):
    """Обрезаю списки только по сравниваемым индексам"""
    O_ = []
    for o_ in O:
        O_.append([o_[i] for i in idexes])
    return O_


def get_equals_objects_idexes(objects):
    equal_indexes = []
    for o in objects:
        indexes = [i for i,v in enumerate(objects) if v==o]  # Получаю индексы равных списков в списке
        equal_indexes.append(indexes)

    equal_indexes = [l for l in equal_indexes if len(l) > 1]  # Удаляю списки длинной меньше 1

    equal_indexes.sort()                                                     #
    equal_indexes = list(num for num,_ in itertools.groupby(equal_indexes))  # Удаляю дубликаты списков в списке
    return equal_indexes


if __name__ == "__main__":
    O1 = [1, 2, 0, 1, 1]
    O2 = [1, 2, 0, 1, 1]
    O3 = [2, 0, 0, 1, 0]
    O4 = [0, 0, 1, 2, 1]
    O5 = [2, 1, 0, 2, 1]
    O6 = [0, 0, 1, 2, 2]
    O7 = [2, 0, 0, 1, 0]
    O8 = [0, 1, 2, 2, 1]
    O9 = [2, 1, 0, 2, 2]
    O9 = [2, 0, 0, 1, 0]
    O10 = [2, 0, 0, 1, 0]
    O = [O1, O2, O3, O4, O5, O6, O7, O8, O9, O10]

    group_idexes = [0, 1, 2] 

    sliced_objects = slice_objects(O, group_idexes) 
    equivalent_objects = get_equals_objects_idexes(sliced_objects)
    print(equivalent_objects)

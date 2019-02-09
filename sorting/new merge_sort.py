import random


def create_list():
    length = random.randint(7, 27)
    new_list = [0] * length
    for i in range(length):
        new_list[i] = random.randint(0, 99)
    return new_list


def check_sorted(a: list, ascending=True):
    s = ascending * 2 - 1
    for i in range(0, len(a)-1):
        if s * a[i] > s * a[i+1]:
            return False
    return True


def merge(a: list, b: list):
    """
    Функция слияния двух отсортированных по возрастанию массивов.
    Принимает на вход два отсортированных массива, возвращает один
    отсортированный массив.
    """
    if not check_sorted(a) or not check_sorted(b):
        return "Что-то пошло не так"
    i = k = n = 0
    c = [0] * (len(a) + len(b))
    while i < len(a) and k < len(b):
        if a[i] < b[k]:
            c[n] = a[i]
            i += 1
        else:
            c[n] = b[k]
            k += 1
        n += 1
    if a[i:]:
        for key in a[i:]:
            c[n] = key
            n += 1
    elif b[k:]:
        for key in b[k:]:
            c[n] = key
            n += 1
    return c


def merge_sort(a: list):
    """
    Сортировка слиянием.
    Принимает на вход массив данных, возвращает отсортированный тот же массив.
    """
    if len(a) < 2:
        return a
    middle = len(a) // 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    c = merge(left, right)
    for i in range(len(c)):
        a[i] = c[i]
    return a


created_list = create_list()
print(created_list, len(created_list))
print(merge_sort(created_list), check_sorted(merge_sort(created_list)))

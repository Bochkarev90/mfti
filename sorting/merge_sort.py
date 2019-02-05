import random


def create_list():
    length = random.randint(7, 27)
    new_list = [0] * length
    for i in range(length):
        new_list[i] = random.randint(0, 99)
    return new_list


def merge(a: list, b: list):
    """
    Функция осуществляет слияние двух отсортированных по возрастанию массивов.
    Принимает на вход 2 списка, возвращает один отсортированный список.
    """
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
        else:
            c[n] = b[k]
            k += 1
        n += 1
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c


def merge_sort(a: list):
    if len(a) <= 1:
        return
    middle = len(a) // 2
    left = [a[i] for i in range(middle)]
    right = [a[i] for i in range(middle, len(a))]
    merge_sort(left)
    merge_sort(right)
    c = merge(left, right)
    for i in range(len(a)):
        a[i] = c[i]


created_list = create_list()
print(created_list, len(created_list))
merge_sort(created_list)
print(created_list, len(created_list))

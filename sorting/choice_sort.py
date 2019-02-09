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


def choice_sort(a: list):
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]


created_list = create_list()
print(created_list, len(created_list))
choice_sort(created_list)
print(created_list, len(created_list), check_sorted(created_list))

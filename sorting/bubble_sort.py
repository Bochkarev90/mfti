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


def bubble_sort(a: list):
    bypass = 0
    for i in range(len(a)):
        for j in range(0, len(a)-1-bypass):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        bypass += 1


created_list = create_list()
print(created_list, len(created_list))
bubble_sort(created_list)
print(created_list, len(created_list), check_sorted(created_list))

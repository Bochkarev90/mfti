import random


def create_list():
    length = random.randint(7, 27)
    new_list = [0] * length
    for i in range(length):
        new_list[i] = random.randint(0, 99)
    return new_list


def hoar_sort(a: list):
    if len(a) <= 1:
        return
    barrier = a[0]
    left = []
    middle = []
    right = []
    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    hoar_sort(left)
    hoar_sort(right)
    k = 0
    for x in left + middle + right:
        a[k] = x
        k += 1


created_list = create_list()
print(created_list, len(created_list))
hoar_sort(created_list)
print(created_list, len(created_list))

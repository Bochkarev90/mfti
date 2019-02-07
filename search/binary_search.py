def left_bound(a: list, key):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(a: list, key):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle] <= key:
            left = middle
        else:
            right = middle
    return right


print(left_bound([0, 1, 2, 3, 3, 3, 4, 8], 5))
print(right_bound([0, 1, 2, 3, 3, 3, 4, 8], 5))

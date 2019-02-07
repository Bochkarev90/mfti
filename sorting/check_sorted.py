def check_sorted(a: list, ascending=True):
    s = ascending * 2 - 1
    for i in range(0, len(a)-1):
        if s * a[i] > s * a[i+1]:
            return False
    return True


def reverse_list(a: list):
    k = len(a)
    for i in range(k // 2):
        a[k-1], a[i] = a[i], a[k-1]
        k -= 1
    return a


new_list = [1, 3, 4, 7, 19, 32, 43, 50, 59, 61, 78, 79, 80, 85, 92, 99]
print(new_list)
print(check_sorted(new_list))
reversed_list = reverse_list(new_list)
print(reversed_list)
print(check_sorted(reversed_list))
print(check_sorted(reversed_list, False))

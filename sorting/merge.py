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


merge([1, 3, 6, 8, 12, 18, 555], [2, 5, 6, 9])
merge([1, 3, 7, 8], [2, 5, 6, 9])

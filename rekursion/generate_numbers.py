def generate_numbers(n: int, m: int, prefix=None):
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m-1, prefix)
        prefix.pop()


# generate_numbers(4, 3)


def generate_permutations(n: int, m: int = -1, prefix=None):
    if m == -1:
        m = n
    prefix = prefix or []
    if m == 0:
        print(*prefix)
        return
    for number in range(1, n + 1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()


generate_permutations(3)

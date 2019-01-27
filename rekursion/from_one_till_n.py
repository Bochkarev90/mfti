def from_one_till_n(n):
    if n == 0:
        return
    from_one_till_n(n - 1)
    print(n, end=' ')


from_one_till_n(18)

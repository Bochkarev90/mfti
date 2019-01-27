def from_a_till_b(a, b):
    if a == b:
        return
    elif a < b:
        from_a_till_b(a, b - 1)
        print(b)
    else:
        print(a)
        from_a_till_b(a - 1, b)


from_a_till_b(38, 18)

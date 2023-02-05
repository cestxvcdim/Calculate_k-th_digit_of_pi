def pi(k):
    n = 10 ** 10_010
    m = p = 2 * n
    i = 1
    while m:
        m = m * i // (2 * i + 1)
        p += m
        i += 1
    return int(str(p)[k])


print(pi(10_000))

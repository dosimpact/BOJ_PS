def c_rotate(c: str):
    return c[-1]+c[:-1]


def cwise_rotate(c: str):
    return c[1:]+c[0]


print(cwise_rotate("hello"))

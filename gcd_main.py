def euclid_algorithm(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


# context managers allows us to allocate and release resources accordingly within our project


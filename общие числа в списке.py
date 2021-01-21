def random(n, m, x, y):
    from random import randint
    lst1 = [randint(0, n) for _ in range(x)]
    lst2 = [randint(0, m) for _ in range(y)]
    print("первый список: ", lst1)
    print("второй список: ", lst2)
    lst3 = set(lst1) & set(lst2)
    lst3 = list(lst3)
    print("третий список:", lst3)
random(50, 30, 10, 60)

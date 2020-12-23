import random


def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)


def get_number_from_index(i, j):
    print("i = ", i)
    print("j = ", j)
    print("= ", i * 4 + j + 1)
    return i * 4 + j + 1


def get_index_from_number(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def insert_2_or_4():
    if random.random() <= 0.75:
        return 2
    else:
        return 4


def get_empty_list(mas):
    empty = []
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def is_zero_in_mas(mas):
    for row in mas:
        if 0 in row:
            return True
    return False

# Надо вычислить сумму цифр в заданном  ряду такого треугольника:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...

def row_sum_odd_numbers(n):

    # Мое решение:
    # start = n * (n-1) + 1
    # my_list = [2 + 2 * i for i in range(n-1)]
    # result = start * n + sum(my_list)
    # return result

    # Чье-то решение:
    # return sum(range(n*(n-1)+1, n*(n+1), 2))

    # А вот гениальное решение:
    return n**3


print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(19))
print(row_sum_odd_numbers(41))

# A Narcissistic Number (or Armstrong Number) is a positive number
# which is the sum of its own digits, each raised to the power of
# the number of digits in a given base. In this Kata, we will restrict
# ourselves to decimal (base 10).
#
# For example, take 153 (3 digits), which is narcissistic:
#
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:
#
#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

# мое решение:
def narcissistic( value ):
    pow = len(str(value))
    result = 0
    for i in str(value):
        result += int(i)**pow
    return True if result==value else False

# чье-то изящное решение:
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))

print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))

# print()
# for i in range(9999999):
#     if narcissistic(i):
#         print(i, end=' ')
# Вывод:
# 0 1 2 3 4 5 6 7 8 9 153 370 371 407 1634 8208 9474 54748
# 92727 93084 548834 1741725 4210818 9800817 9926315

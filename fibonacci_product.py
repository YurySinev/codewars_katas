# Функция принимает число. Необходимо выяснить, является ли
# это число произведением двух последовательных чисел Фибоначчи.
# Мое решение:
# def product_fib(prod):
#     a, b = 0, 1
#     while True:
#         if a * b == prod: return [a, b, True]
#         if a * b > prod: return [a, b, False]
#         a, b = b, a + b


# чье-то изящное решение:
# def product_fib(prod):
#     a, b = 0, 1
#     while prod > a * b:
#         a, b = b, a + b
#     return [a, b, prod == a * b]

# А вот еще более классное решение:
def product_fib(prod):
    func = lambda a, b: func(b, a+b) if a*b < prod else [a, b, a*b == prod]
    return func(0, 1)


if __name__ == '__main__':
    print(product_fib(4895))
    print(product_fib(5895))
    print(product_fib(12816))
    print(product_fib(33551))
    print(product_fib(33552))

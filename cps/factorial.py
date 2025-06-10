def fact_cps(n, succ):
    if n == 1:
        return succ(1)
    else:
        return fact_cps(n - 1, lambda x: succ(n * x))


fact_cps(100, lambda x: x)


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# factorial(100)

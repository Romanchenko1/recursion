def fibonacci(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def  power2(n):#вычисление степени
    if n != 0:
        return 2 * power2(n - 1)
    else:
        return 1


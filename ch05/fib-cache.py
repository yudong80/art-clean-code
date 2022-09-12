cache = dict()

def fib(n):
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    fib_n = fib(n-1) + fib(n-2)
    cache[n] = fib_n
    return fib_n


print(fib(100))
# 354224848179261915075
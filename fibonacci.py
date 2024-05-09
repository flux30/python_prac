def fibonacci_series(n):
    fib_series = [0, 1]
    while fib_series[-1] + fib_series[-2] <= n:
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
    return fib_series

limit = int(input("Enter a number to print Fibonacci series up to: "))

fibonacci_nums = fibonacci_series(limit)
print("Fibonacci series up to", limit, ":", fibonacci_nums)

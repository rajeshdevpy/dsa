# 0, 1, 1, 2, 3, 5, 8, 13, 21, .............
# using Third variable and for loop
def fibonacci_series(number):
    a, b = 0, 1
    fib_series = [0]
    for i in range(number):
        c = a + b
        a = b
        b = c
        fib_series.append(a)
    return fib_series

# print(fibonacci_series(10))

# Without using third variable
def fibonacci_series1(number):
    a, b = 0, 1
    if number == 1:
        return [0]
    else:
        fib_series = [0]
        while b <= number:
            a, b = b, a + b
            fib_series.append(a)
    return fib_series


# print(fibonacci_series1(10))

# using recursive function
def fibonacci(n):
    if n <= 1:
        return n
    return (fibonacci(n-1)+fibonacci(n-2))

n = 10
if n <= 0:
    print("Invalid")
else:
    for i in range(n):
        print(fibonacci(i))

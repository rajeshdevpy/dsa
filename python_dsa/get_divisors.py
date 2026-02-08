# Print the Factors or Divisors of a given number
# 10 = [1, 2, 5, 10]
# 15 = [1, 3, 15]
# 25 = [1, 5, 25]
# 7 = [1, 7]
# 19 = [1, 19]

from math import sqrt

# version 1
def get_factors(number):
    factors = [1]
    for num in range(2, number + 1):
        if number % num == 0:
            factors.append(num)
    return factors


if __name__ == "__main__":
    number = 15
    print(get_factors(number))


# version 2 --> using sqrt function


# Understands 
# 1. Hashmap concept
# 2. Recursion concept
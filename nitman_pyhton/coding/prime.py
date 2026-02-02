# 2, 3, 5, 7, ............

def primes(start, end):
    for n in range(start, end):
        if n > 1:
            for i in range(2, (n//2 + 1)):
                if n % i == 0:
                    break
            else:
                print(n)
        else:
            pass
primes(1, 10)
# n = 234
n = 121

num = n
result = 0
while num > 0:
    ld = num % 10
    result = (result * 10) + ld
    num = num // 10
if result == n:
    print("Yes")
else:
    print("No")

"""
TC --> O(log base10(N))
SC --> O(1)
"""
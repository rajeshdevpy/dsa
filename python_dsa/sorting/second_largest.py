nums = [55, 32, 97, -55, 45, 32, 88, 21]
largest = float("-inf")
s_largest = float("-inf")

for num in nums:
    if num > largest:
        s_largest = largest
        largest = num
    elif num > s_largest and num != largest:
        s_largest = num
print(s_largest)
        

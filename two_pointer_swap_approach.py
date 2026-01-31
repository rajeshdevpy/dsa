NUMS = [1, 2, 4, 5, 3, 6]

left = 0
right = len(NUMS) - 1

while left < right:
    NUMS[left], NUMS[right] = NUMS[right], NUMS[left]
    left += 1
    right -= 1

print(NUMS)
nums = [4, 9, 10, 11, 12, 16]
def is_sorted(nums):
    for i in range(len(nums) - 1):
        print(i)
        if nums[i] > nums[i + 1]:
            return False
    return True
print(is_sorted(nums))
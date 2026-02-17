nums = [1, -2, 7, 5, 4, 2, 3]
nums2 = [5, 2, 3, 10, 3, 10, 5]
nums3 = [10, 20, 5, 7]

def get_target_idx(nums, target=3):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == target:
            return i
    return -1

print(get_target_idx(nums, target=3))
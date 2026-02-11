nums = [7, 3, 8, 4, 6, 2, 9, 1]

def selection_sort(nums):
    for i in range(0, len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

print(selection_sort(nums))

nums = [1, 2, 3, 4, 5, 6]
target =  5
# output = 1
# Note: Binary search algorithm only work for sorted elemnets in a list/array
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return -1

print(binary_search(nums, target))


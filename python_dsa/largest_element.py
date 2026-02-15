nums = [-33, 20, 1, 55, 66, 76, 12]
def get_longest(nums):
    largest_num = nums[0]
    largest_num = float("-inf")
    for num in nums:
        # if num > largest_num:
        #     largest_num = num
        largest_num = max(largest_num, num)
    return largest_num
print(get_longest(nums))
def get_natural_number_upto(n, current=1):
    if current > n:
        return 
    print(current)
    return get_natural_number_upto(n, current+1)

# print(get_natural_number_upto(5))



def get_factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * get_factorial(num - 1)

# print(get_factorial(5))

def reverse_list_elements(nums, left, right):
    if left >= right:
        return nums
    nums[left], nums[right] = nums[right], nums[left]
    return reverse_list_elements(nums, left + 1, right -1)

# print(reverse_list_elements([9, 2, 5, 4, 1, 0, 7], 0, 6))

def check_palindrome(str_val, left, right):
    if left >= right:
        return True
    if str_val[left] != str_val[right]:
        return False
    return check_palindrome(str_val, left + 1, right - 1)

str_val1 = "nitin"
str_val = "nitinq"
print(check_palindrome(str_val, 0, len(str_val) - 1))

# Head and tail recurssion, backtracking, stacked space

def get_fibonacci_series():
    pass
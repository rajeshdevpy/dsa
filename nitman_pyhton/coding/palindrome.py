#===== String type of question======#

inp1 = "NITIN"
# Using split method
def palindrome(inp1):
    if inp1[::-1] == inp1:
        return True
    return False

# using for loop
def palindrome2(inp1):
    n = len(inp1)
    for i in range(n):
        if inp1[i] != inp1[n - i - 1]:
            return False
    return True
            

# Using while loop
def palindrome3(inp1):
    n = len(inp1)
    first = 0
    last = n - 1
    while first < last:
        if inp1[first] == inp1[last]:
            first += 1
            last -= 1
        else:
            return False
        
    return True    

# Using in-built reversed and join function
def palindrome4(inp1):
    temp = "".join(reversed(inp1))
    if temp == inp1:
        return True
    return False

# =====Number type of question=====#
def palindrome5(number):
    temp = number
    reversed_num = 0
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp = temp // 10
    if reversed_num == number:
        return True, number, reversed_num
    return False, number, reversed_num

print(palindrome5(121))
print(palindrome5(125))
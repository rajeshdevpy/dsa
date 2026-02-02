# Compress String
# aabbccddeeee = a2b2c2d2e4

# Input =  aabbccaaaafffeiii
# Output = a2b2c2a4f3e1i3

# Using for loop
def compress(inp):
    n = len(inp) - 1
    new_str = ""
    count = 1
    for i in range(n):
        if inp[i] == inp[i+1]:
            count += 1
        else:
            new_str += inp[i] + str(count)
            count = 1
    if count:
        new_str += inp[-1] + str(count)
    return new_str

print(compress("aabbccaaaafffeiii"))

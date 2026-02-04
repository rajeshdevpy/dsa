# s = "abcabcabczxe"
s = "bbbbb"

max_len = 0
result = ""

for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        if s[j] in temp:
            break
        temp += s[j]
    if len(temp) > max_len:
        max_len = len(temp)
        result = temp
print(result, max_len)


# using sliding window
s = "bbbb"

char_set = set()
left = 0
max_length = 0
result = ""

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1

    char_set.add(s[right])

    if right - left + 1 > max_length:
        max_length = right - left + 1
        result = s[left:right+1]

print(result, max_length)

# 4️⃣ Interview one-liners

# Anagram:

# “Two strings containing the same characters with the same frequency, regardless of order.”

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True


# Pangram:

# “A sentence that includes every letter of the alphabet at least once.”
import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(sentence.lower()))

print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True


# get digits from below string and sum up those
def sum_of_digits(str_val):
    num = ""
    nums = []
    for i in str_val:
        if i.isdigit():
            num += i
        else:
            if num:
                nums.append(int(num))
                num = ""
    if num:
        nums.append(int(num))
        return sum(nums)
    
print(sum_of_digits("/hjgnk12gfyiunb.>@13tfoupiy10"))
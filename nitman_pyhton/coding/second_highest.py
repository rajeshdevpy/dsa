# Without using any built-in functions (BEST for interviews)
nums = [10, 5, 20, 8, 15]

largest = float('-inf')
second_largest = float('-inf')

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print(second_largest)
"""
Why this is strong
O(n) time
O(1) space
Handles duplicates
Shows algorithmic thinking
"""

# 2️⃣ Using sort() (simple but less optimal)

nums = [10, 5, 20, 8, 15]
nums = list(set(nums))   # remove duplicates
nums.sort()

print(nums[-2])
# ⛔ Time: O(n log n)
# ⛔ Uses extra space

# 3️⃣ Using built-in functions (Pythonic)
nums = [10, 5, 20, 8, 15]
print(sorted(set(nums))[-2])


# ✔ Clean
# ⛔ Sorting overhead

# -------------------------------------
# 4️⃣ Using heapq (good for large data)
import heapq

nums = [10, 5, 20, 8, 15]
print(heapq.nlargest(2, set(nums))[1])


# ✔ Efficient for streaming data
# ✔ Used in real systems

# 5️⃣ Edge case handling (IMPORTANT)
def second_highest(nums):
    if len(set(nums)) < 2:
        return None
    largest = second = float('-inf')

    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:
            second = n
    return second

"""🧠 Interview Answer (What to say)

“I iterate once while tracking the largest and second largest values.
If the current number exceeds the largest, I update both.
This gives O(n) time and O(1) space complexity.”"""
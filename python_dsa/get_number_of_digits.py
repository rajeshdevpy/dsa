n = 543211
num = n  # Always do changes in another variable not in input variable
count = 0
while num > 0:
    count += 1
    num = num // 10
print("Count", count)
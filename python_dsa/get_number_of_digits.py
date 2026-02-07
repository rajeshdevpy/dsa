n = 543211
num = n  # Always do changes in another variable not in input variable
count = 0
while num > 0:
    count += 1
    num = num // 10
print("Count", count)

# Extract digit from a number and return a list contaning those elements
def get_result(n):
    result = []
    num = n

    while num > 0:
        ld = num % 10
        result.append(ld)
        num = num // 10
    # return result
    return result[::-1]

if __name__ == "__main__":
    result = get_result(n)
    print(result)
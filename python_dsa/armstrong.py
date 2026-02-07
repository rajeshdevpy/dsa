def is_armstrong_number(number):
    num = number
    nod = len(str(number))
    total = 0
    while num > 0:
        ld = num % 10
        total += ld ** nod
        num = num // 10
    if total == number:
        return True
    return False



if __name__ == "__main__":
    number = 151
    print(is_armstrong_number(number))
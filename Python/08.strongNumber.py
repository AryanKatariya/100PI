def facto(num):
    if (num == 0):
        return 1

    return num * facto(num - 1)

def detectStrong(num):
    sum = 0
    temp = num
    while (temp != 0):
        digit = temp % 10
        sum = sum + facto(digit)
        temp /= 10

    return sum == num

num = 145

if (detectStrong(num)):
    print(num, " is Strong Number")
else:
    print(num, " is not a Strong Number")

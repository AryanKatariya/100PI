num = 8
k = 0
for i in range(1, num + 1):
    # printing left spaces in rows
    for j in range(i, num):
        print(" ", end="")

    while k != (2 * i - 1):
        # printing left/right boundaries
        if k == 0 or k == 2 * i - 2:
            print("*", end="")
        # printing spaces in the middle of the triangle
        else:
            print(" ", end="")
        k = k + 1

    k = 0
    print()

# printing bottom boundary of the triangle
for i in range(0, 2 * num - 1):
    print("*", end="")
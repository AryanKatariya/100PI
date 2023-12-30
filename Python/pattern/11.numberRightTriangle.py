num = int(input("Enter the Number: "))
k = 1
for i in range(0, num):
    for j in range(0, i+1):
        print(k, end="")
        k = k+1
    print()
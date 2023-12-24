side = int(input("Enter side:"))

for i in range(0,side):
    for j in range(0,side):
        if(i==0 or j==0) or (i==side-1 or j==side-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
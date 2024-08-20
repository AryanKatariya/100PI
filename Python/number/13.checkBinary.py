num=str(input("Enter a number:"))

def isBinary(n):
    return n.isdigit() and all(i in '01' for i in n)

print(isBinary(num))
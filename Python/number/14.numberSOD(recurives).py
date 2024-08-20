num=str(input("Enter a number:"))

l = list(num)

def SOD(l):
    if len(l) == 1:
        return int(l[0])
    
    return int(SOD(l[0])) + SOD(l[1:])

def SumofDigits(n):
    if n == 0:
        return 0
    
    return n%10 + SumofDigits(n//10)

print(SOD(l))
print(SumofDigits(int(num)))
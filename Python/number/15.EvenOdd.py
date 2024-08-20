num=int(input("Enter a number:"))

def EvenOdd(n):
    if n&1:
        return "Odd"
    else:
        return "Even"
    
print(EvenOdd(num))
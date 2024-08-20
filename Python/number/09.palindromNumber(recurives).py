num=str(input("Enter a number:"))

def palindromeNumber(n):
    if len(n) < 1:
        return True
    
    if n[0] == n[-1]:
        return palindromeNumber(n[1:-1])
    else:
        return False
    
print(palindromeNumber(num))
def reverseNumber(n):
    num = n
    reverse = 0
    
    while(num>0):
        rem = num%10
        reverse = reverse*10+rem
        num = num//10
        
    return reverse

def recurReverseNumber(n,reverse):
    if n == 0:
        return reverse
    rem = n%10
    reverse = reverse*10+rem
    n = n//10
    return recurReverseNumber(n,reverse)

n = 12345
reverse = 0
print(reverseNumber(n))
print(recurReverseNumber(n,reverse))
print(int(str(n)[::-1]))
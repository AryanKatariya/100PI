def primeCheck(n):
    if(n <= 1):
        return False
    
    for i in range(2,int(n/2)+1):
        if(n%i == 0):
            return False
    
    return True

def isPrime(n):
    if(n <= 1):
        return False
    
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0:
            return False
    
    return True

n = 17
print(primeCheck(n))
print(isPrime(n))
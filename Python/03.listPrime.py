def isPrime(n):
    if(n <= 1):
        return False
    
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0:
            return False
    
    return True

def listPrime(n):
    prime = []
    for i in range(n):
        if(i == 2):
            prime.append(i)
            continue
            
        flag = isPrime(i)
        if(flag):
            prime.append(i)
            
    return prime

n = 10
print(listPrime(n))
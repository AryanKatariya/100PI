def armNumber(n):
    num = n
    digit = 0
    sum = 0
    l = len(str(num))
    
    for i in range(l):
        digit = int(num%10)
        num = num/10
        sum += pow(digit,l)
        
    return sum

n = 371
sum = armNumber(n)
if sum==n:
  print("Armstrong")
else:
  print("Not Armstrong")
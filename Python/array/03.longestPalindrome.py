def isPalindrome(n):

   divisor = 1
   while (int(n / divisor) >= 10):
      divisor *= 10

   while (n != 0):
      leading = int(n / divisor)
      trailing = n % 10

      if (leading != trailing):
         return False

      n = int((n % divisor) / 10)

      divisor = int(divisor / 100)
   return True

def largestPalindrome(A, n) :
   A.sort()

   for i in range(n - 1, -1, -1) :
      if (isPalindrome(A[i])) :
            return A[i]    

   return -1

arr = [1, 232, 5545455, 909090, 161]
n = len(arr) 
print(largestPalindrome(arr, n))
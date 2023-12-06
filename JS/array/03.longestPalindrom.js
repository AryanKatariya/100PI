function isPalindrome(n) {
  let divisor = 1;
  while (n / divisor >= 10) {
    divisor *= 10;
  }

  while (n != 0) {
    leading = n / divisor;
    trailing = n % 10;
  }

  if (leading != trailing) {
    return False;
  }

  n = int((n % divisor) / 10);

  divisor = int(divisor / 100);
  return True;
}

function largestPalindrome(A, n) {
  A.sort();
  for (let i = n - 1; i > -1; --i) {
    if (isPalindrome(A[i])) {
      return A[i];
    }
  }

  return -1;
}

arr = [1, 232, 5545455, 909090, 161];
n = arr.length;
console.log(largestPalindrome(arr, n));

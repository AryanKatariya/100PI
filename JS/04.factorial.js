function getFactorial(n) {
  if (n == 0) {
    return 1;
  }

  return n * getFactorial(n - 1);
}

var n = 6;
console.log(getFactorial(n));

// n/2
function checkPrime(n) {
  if (n <= 1) {
    return false;
  }

  for (let i = 2; i < n / 2 + i; i++) {
    if (n % i == 0) {
      return false;
    }
  }

  return true;
}

//Squart Root of N
function isPrime(n) {
  if (n <= 1) {
    return false;
  }

  for (let i = 2; i < Math.sqrt(n) + 1; i++) {
    if (n % i == 0) {
      return false;
    }
  }

  return true;
}

// Skipping Even number
var ans = (n) => {
  if (n <= 1) {
    return false;
  }

  if (n == 2) {
    return true;
  }

  if (n % 2 == 0) {
    return false;
  }

  for (let i = 3; i <= Math.sqrt(n); i += 2) {
    if (n % i == 0) return false;
  }

  return true;
};

let n = 6;
console.log(checkPrime(n));
console.log(isPrime(n));
console.log(ans(n));

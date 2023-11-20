function listPrime(n) {
  let prime = [];

  for (let i = 2; i < n; i++) {
    let flag = true;
    // if (i == 2) {
    //   prime.push(i);
    // }

    for (let x = 2; x < i; x++) {
      if (i % x == 0) {
        flag = false;
      }
    }
    if (flag == true) {
      prime.push(i);
    }
  }

  return prime;
}

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

function effListPrime(n) {
  var prime = [];

  for (let i = 1; i < n; i++) {
    if (i == 2) {
      prime.push(i);
      continue;
    }
    flag = isPrime(i);
    if (flag) {
      prime.push(i);
    }
  }
  return prime;
}

var n = 100;
// console.log(listPrime(n));
console.log(effListPrime(n));

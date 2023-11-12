function reverseNumber(n) {
  let num = n;
  let reverse = 0;

  while (n != 0) {
    let x = n % 10;
    reverse = reverse * 10 + x;
    n = Math.floor(n / 10);
  }

  return reverse;
}

function recurReverseNumber(n, reverse) {
  if (n == 0) {
    return reverse;
  }
  rem = n % 10;
  reverse = reverse * 10 + rem;
  n = Math.floor(n / 10);

  return recurReverseNumber(n, reverse);
}

var ans = (n) => {
  return parseFloat(n.toString().split("").reverse().join(""));
};

var n = 1234;
var reverse = 0;
console.log(reverseNumber(n));
console.log(recurReverseNumber(n, reverse));
console.log(ans(n));

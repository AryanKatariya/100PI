function armNumber(n) {
  var num = n;
  let digit = 0;
  let sum = 0;
  let l = num.toString().length;

  for (let i = 0; i < l; i++) {
    digit = num % 10;
    num = num / 10;
    sum += Math.pow(digit, l);
  }

  return sum;
}

let n = 371;
let sum = armNumber(n);
if (sum == n) {
  console.log("Armstrong");
} else {
  console.log("Not Armstrong");
}

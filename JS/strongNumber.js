function facto(num) {
  if (num == 0) {
    return 1;
  }

  return num * facto(num - 1);
}

function detectStrong(num) {
  let digit;
  let sum = 0;
  let temp = num;

  while (temp != 0) {
    digit = temp % 10;

    sum = sum + facto(digit);
    temp /= 10;
  }

  return sum == num;
}

var num = 145;

if (detectStrong(num)) console.log(num, " is Strong Number");
else console.log(num, " is not a Strong Number");

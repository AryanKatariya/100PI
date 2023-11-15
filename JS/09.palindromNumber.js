var isPalindrome = function (x) {
  const reverseNum = parseInt(x.toString().split("").reverse().join(""), 10);
  return x === reverseNum;
};

n = 121;
console.log(isPalindrome(n));

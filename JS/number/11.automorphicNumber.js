function autoNumber(n) {
  var s = Math.pow(n, 2);
  var m = Math.pow(10, n.toString().length);
  if (s % m == n) {
    console.log("It's an Automorphic Number");
  } else {
    console.log("It's not an Automorphic Number");
  }
}

autoNumber(376);
autoNumber(377);

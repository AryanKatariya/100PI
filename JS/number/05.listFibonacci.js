function listFib(n) {
  if (n <= 1) {
    return n;
  }
  return listFib(n - 1) + listFib(n - 2);
}

var n = 10;
var array = [];
for (let i = 0; i < n; ++i) {
  array.push(listFib(i));
}
console.log(array);

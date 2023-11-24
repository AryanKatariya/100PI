function countDistinct(arr, n) {
  arr.sort();

  i = 0;
  while (i < n) {
    count = 1;

    while (i < n - 1 && arr[i] == arr[i + 1]) {
      i += 1;
      count += 1;
    }
    console.log(arr[i], count);
    i += 1;
  }
}

arr = [5, 8, 5, 7, 8, 10];
n = arr.length;
countDistinct(arr, n);

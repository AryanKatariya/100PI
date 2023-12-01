function minOperations(nums) {
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] <= nums[i - 1]) {
      d = Math.abs(nums[i] - nums[i - 1]) + 1;
      nums[i] += d;
    }
  }
  return nums;
}

console.log(minOperations([1, 5, 2, 4, 1]));

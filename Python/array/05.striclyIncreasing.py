def minOperations(nums):
        # ans = 0
        for i in range(1,len(nums)):
            if(nums[i]<=nums[i-1]):
                d = abs(nums[i]-nums[i-1])+1
                # ans += d
                nums[i] += d
                
        return nums
    
print(minOperations([1,5,2,4,1]))
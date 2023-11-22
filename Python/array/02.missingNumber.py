def findDisappearedNumbers(nums):
    set_nums = set(nums)
    missing = []

    for i in range(1,len(nums)+1):
        if i not in set_nums:
            missing.append(i)

    return missing

nums = [1,2,4,5,6,7,1,9]
print(findDisappearedNumbers(nums))
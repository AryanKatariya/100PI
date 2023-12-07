def removeDuplicates(arr):
    for i in arr:
        if arr.count(i)>1:
            arr.remove(i)
        
    return arr

l = [10, 20, 40, 30, 50, 20, 10, 20]
arr = removeDuplicates(l)
print(sorted(arr))
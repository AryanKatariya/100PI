def disjoint(arr1,arr2):
    l1 = set(arr1)
    l2 = set(arr2)
    if(l1.intersection(l2)):
        print("Not a disjoint ")
    else:
        print("disjoint")
        
arr1 = [10, 5, 3, 4, 6]
arr2 = [8, 7, 9]
disjoint(arr1,arr2)
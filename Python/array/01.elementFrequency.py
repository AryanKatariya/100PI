def countDistinct(arr, n):
    arr.sort()

    i = 0
    while i < n:
        count = 1

        while i < n - 1 and arr[i] == arr[i + 1]:
            i += 1
            count +=1

        print("{0}: {1}".format(arr[i], count))
        i += 1

arr = [5, 8, 5, 7, 8, 10]
n = len(arr)
countDistinct(arr, n)
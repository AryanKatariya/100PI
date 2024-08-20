def countEachChar(file):
    count={}
    with open(file,'r') as f:
        for lines in f:
            for char in lines:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
    return count

filePath = "example.txt"
print(countEachChar(filePath))

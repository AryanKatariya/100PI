def countNumber(s):
    sum=0
    for i in s:
        if i.isnumeric():
            sum+=int(i)
    return sum

s = 'a1er2e3e6df8fd4df6'
print(countNumber(s))
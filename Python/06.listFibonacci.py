def listFib(n):
  if (n <= 1):
    return n
  return listFib(n - 1) + listFib(n - 2)


n = 10
array = []
for i in range(n):
#   array.append(listFib(i))
    print(listFib(i),end=" ")
  
# print(array)

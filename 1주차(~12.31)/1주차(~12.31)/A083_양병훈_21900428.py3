num = input()
temp = list(map(int, input().split()))
res = []

for i in range(len(temp)):
  if temp[i] not in res:
    res.append(temp[i])

res.sort()
for i in range(len(res)):
  print(res[i], end=" ")
num = [0 for row in range(3)]
for i in range(3):
  num[i] = int(input())
res = num[0]*num[1]*num[2]
res = str(res)

count = [0 for row in range(10)]
for i in range(10):
  for j in range(len(res)):
    if str(i) == res[j]:
      count[i] += 1

for i in range(10):
  print(count[i])
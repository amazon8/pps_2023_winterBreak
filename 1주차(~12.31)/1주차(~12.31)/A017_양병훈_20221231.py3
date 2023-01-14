import math

num = input()
count = [0 for col in range(10)]
for i in range(len(num)):
  for j in range(10):
    if num[i] == str(j):
      count[j] += 1

count[6] += count[9]
count[6] = math.ceil(int(count[6])/2)
count[9] = 0

res = max(count)
print(res)
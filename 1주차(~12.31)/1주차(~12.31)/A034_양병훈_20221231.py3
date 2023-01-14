num = [[0 for col in range(1)]for row in range(10)]
for i in range(10):
  num[i] = int(input())
  num[i] = num[i] % 42

res = [0 for col in range(42)]

for i in range(10):
  if res[num[i]] == 0:
    res[num[i]]=1

print(sum(res))
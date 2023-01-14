num = int(input())

res = []
for i in range(num):
  temp = input()
  res.append(temp)

for i in range(num):
  sums = 0
  rightFlag = 0
  for j in range(len(res[i])):
    if res[i][j] == "O":
      rightFlag += 1
      sums += rightFlag
    else:
      rightFlag = 0
  print(sums)
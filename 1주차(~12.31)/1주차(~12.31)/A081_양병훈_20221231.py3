num = int(input())

test = []
for i in range(num):
  temp = map(int, input().split())
  temp = list(temp)
  temp.sort(reverse=True)
  test.append(temp)

for i in range(num):
  print(test[i][2])
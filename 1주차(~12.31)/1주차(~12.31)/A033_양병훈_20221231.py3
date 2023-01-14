score = [[0 for col in range(4)]for row in range(5)]

for i in range(5):
  score[i] = map(int, input().split())
  score[i] = list(score[i])
  

sums = 0
index = 0 

for i in range(5):
  if sums < sum(score[i]):
    sums = sum(score[i])
    index = i+1

print(index, sums)
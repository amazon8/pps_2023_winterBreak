num = int(input())
plug = []
for i in range(num):
  temp = int(input())
  plug.append(temp)

sums = sum(plug)
sums = sums - num +1
print(sums)
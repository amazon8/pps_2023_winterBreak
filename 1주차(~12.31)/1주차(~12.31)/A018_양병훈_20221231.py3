num = input()
a = map(int, input().split())
a = list(a)
b = map(int, input().split())
b = list(b)

a.sort()
sum = 0
for i in range(len(a)):
  sum += a[i] * max(b)
  b.remove(max(b))
  

print(sum)
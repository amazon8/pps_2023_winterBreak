num = int(input())
name = []
for i in range(num):
  temp = input()
  name.append(temp)

alpha = [0 for col in range(26)]
for i in range(num):
  temp = ord(name[i][0])
  alpha[temp-97] += 1

empty = 1
for i in range(26):
  if alpha[i] >= 5:
    print(chr(i+97), end="")
    empty =0 
if empty == 1:
  print("PREDAJA")
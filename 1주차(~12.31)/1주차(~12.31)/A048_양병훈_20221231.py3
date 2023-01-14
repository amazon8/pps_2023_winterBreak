num = int(input())
word = []
for i in range(num):
  temp = input()
  word.append(temp)

res = 0
for i in range(num):
  alpha = [0 for col in range(26)]
  exChr = ""
  groupFlag = 1
  for j in range(len(word[i])):
    if exChr != word[i][j]:
      if alpha[ord(word[i][j])-97] != 0:
        groupFlag = 0
        break  
      else:
        exChr = word[i][j]
        alpha[ord(word[i][j])-97] += 1
    else:
      exChr = word[i][j]
      alpha[ord(word[i][j])-97] += 1
        
  if groupFlag == 1:
    res += 1

print(res)
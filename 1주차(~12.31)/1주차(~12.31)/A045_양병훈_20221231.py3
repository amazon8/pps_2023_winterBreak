word = input()
word = word.lower()

alpha = [0 for col in range(26)]

for i in range(len(word)):
  alpha[ord(word[i])-97] += 1

tempMax = max(alpha)
num = alpha.count(tempMax)

if num > 1:
  print("?")
else:
  print(chr(alpha.index(tempMax)+65))
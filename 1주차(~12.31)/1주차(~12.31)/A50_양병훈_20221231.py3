word = input()
word = list(word)
for i in range(len(word)):
  temp = ord(word[i])-3
  if temp < 65:
    if 64 == temp:
      word[i] = "Z"
    elif 63 == temp:
      word[i] = "Y"
    elif 62 ==temp:
      word[i] = "X"
  else:
    word[i] = chr(temp)

print("".join(word))
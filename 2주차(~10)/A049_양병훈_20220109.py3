vowel = ["a","e","i","o","u"]


while 1:
  word = input()
  acceptFlag = 1
  exFlag = ""
  vowelNum = 0
  consonantNum = 0  
  if word == "end":
    break
  for i in range(len(vowel)):
    if vowel[i] in word:
      vowelNum += 1
  if vowelNum == 0:
    acceptFlag = 0

  vowelNum = 0    
  for i in range(len(word)):
    if  word[i] in vowel:
      vowelNum += 1
      consonantNum =0
    else:
      consonantNum += 1
      vowelNum = 0
    if vowelNum == 3 or consonantNum ==3:
      acceptFlag = 0
      break

    if exFlag != word[i]:
      exFlag = word[i]
    else:
      if exFlag == "e":
        exFlag = "e"
      elif exFlag =="o":
        exFlag = "o"
      else:
        acceptFlag = 0
        break

  if acceptFlag == 0:
    print("<" + word + "> is not acceptable.")
  else:
    print("<" + word + "> is acceptable.")    
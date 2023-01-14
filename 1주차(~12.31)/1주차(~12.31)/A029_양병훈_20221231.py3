num = int(input())
exNum = int(input())
if num >= 6:
  print("Love is open door")
else:
  for i in range(1, num):
    if exNum == 0:
      print(1)
      exNum = 1
    else:
      print(0)
      exNum = 0
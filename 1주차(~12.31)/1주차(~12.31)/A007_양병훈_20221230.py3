"""
시작: 11:06
종료:

1. 입력
2. 첫 문자로 flag 설정
3. flag --> asc, desc 판단
"""

scale = map(int, input().split())
scale = list(scale)
if scale[0]== 1:
  tempAscendingFlag=1
elif scale[0]==8:
  tempAscendingFlag = 0
else:
  tempAscendingFlag =2

AscendingFlag=2
rightNum=0
if tempAscendingFlag==1:
  for i in range(8):
    if scale[i] == i+1:
      rightNum += 1
  if rightNum == 8:
    AscendingFlag = 1

if tempAscendingFlag==0:
  for i in range(8):
    if scale[i] == 8-i:
      rightNum += 1
  if rightNum == 8:
    AscendingFlag = 0

if AscendingFlag==0:
  print("descending")
elif AscendingFlag==1:
  print("ascending")
else:
  print("mixed")
